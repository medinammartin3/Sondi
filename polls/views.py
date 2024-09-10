from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CodeForm, QuestionForm, ChoiceFormSet
from .models import Choice, Question

import os
import datetime
import json
from cuid2 import Cuid
from hashids import Hashids
from dotenv import load_dotenv

load_dotenv()

# Initialize Hashids with the provided salt and minimum length
hashids = Hashids(salt=os.getenv("HASHID_SALT"), min_length=8)

# Unique code generation with CUID2
# Max (total) entropy : 1,572,120,576
# Before reaching 50% chance of collision : ~ 39,650
CUID_GENERATOR: Cuid = Cuid(length=6)



"""
View for the Polls app index page.
Displays a form for searching polls by code and the lists public questions.
"""
class IndexView(generic.ListView, generic.FormView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    form_class = CodeForm

    # Get the public questions by category.
    # Excludes questions scheduled to be published in the future.
    def get_queryset(self):
        # Return the last 20 published questions.
        most_recent = Question.objects.filter(visibility='public',
                                                pub_date__lte=timezone.now()
                                                ).order_by("-pub_date")[:20]
        # Return the 20 all-time most voted questions.
        most_voted = Question.objects.filter(visibility='public',
                                                pub_date__lte=timezone.now()
                                                ).annotate(total_votes=Sum('choice__votes')
                                                ).order_by('-total_votes')[:20]
        # Return the questions published in the last 24 hours.
        questions_last24h = Question.objects.filter(visibility='public',
                                                    pub_date__lte=timezone.now(),
                                                    pub_date__gte=timezone.now() - datetime.timedelta(days=1))
        # Return the 20 most voted questions in the last 24 hours.
        trending = questions_last24h.annotate(total_votes=Sum('choice__votes'),
                                                ).order_by('-total_votes')[:20] 
        # Return 20 random questions.
        random = Question.objects.filter(visibility='public',
                                            pub_date__lte=timezone.now()
                                            ).order_by('?')[:20]
        return (most_recent, most_voted, trending, random)
    
    # Add to the context the form and the public questions.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Search form
        context['form'] = self.get_form()
        # Public questions by category
        most_recent, most_voted, trending, random = self.get_queryset()
        context['most_recent'] = most_recent
        context['most_voted'] = most_voted
        context['trending'] = trending
        context['random'] = random
        return context

    # Get the succes url passing the question code on the arguments.
    def get_success_url(self):
        code = self.form.cleaned_data['question_code'] 
        return reverse('polls:vote', kwargs={'question_code': code})

    def form_valid(self, form):
        self.form = form
        return super().form_valid(form)
   


"""
View for handling poll voting.
"""
@login_required
def vote(request, question_code):
    try:
        question = Question.objects.get(code=question_code)
    except Question.DoesNotExist:
        # Render custom 404 (poll not found) template
        return render(request, 'errors/poll_not_found.html', status=404)
    user = request.user

    # Initialize the voted_questions field on the JSON if it's not already set 
    if 'voted_questions' not in user.voted_questions:
        user.voted_questions['voted_questions'] = []

    # Get the current list of voted question codes
    voted_questions = user.voted_questions['voted_questions']

    # Check if the user has already voted for this question
    if question_code in voted_questions:
        # Render custom 403 (revote error) template
        return render(request, 'errors/revote_error.html', status=403)
    # The user can vote
    else:
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Display error message only if the form is submitted.
            if request.method == "POST":
                return render(
                    request,
                    "polls/vote.html",
                    {
                        "question": question,
                        "error_message": "Please select a choice",
                    },
                )
            else:
                return render(request, "polls/vote.html", {"question": question})
        else:
            # Using F() expression to avoid race condition
            selected_choice.votes = F('votes') + 1 
            selected_choice.save()

            # Add the question code to the user's voted questions list
            voted_questions.append(question_code)
            user.voted_questions['voted_questions'] = voted_questions
            user.save()  # Save the updated user object

            # HttpResponseRedirect after successfully dealing with POST data
            # to prevent multiple submissions.
            return HttpResponseRedirect(reverse("polls:vote_results", args=[hashids.encode(question.id)]))
    


"""
View for displaying poll results after voting.
"""
class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/vote_results.html"

    def get_object(self):
        try:
            encoded_id = self.kwargs.get('encoded_id')
            # Decode the encoded_id using Hashids
            id = hashids.decode(encoded_id)[0]
            # Fetch the student instance by the decoded ID
            question = Question.objects.get(pk=id)
            return question
        except (IndexError, Question.DoesNotExist):
            raise Http404("Question not found")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()

        # Calculate total votes for the poll.
        total_votes = question.choice_set.aggregate(total_votes=Sum('votes'))['total_votes']
        context['total_votes'] = total_votes

        # Prepare data points for the results graph.
        datapoints = []
        if total_votes > 0:  # Avoid division by zero
            for choice in question.choice_set.all():
                # Calculate the percentage of total votes each choice received
                votes_percentage = choice.votes*100/total_votes
                datapoints.append({"label": choice.choice_text, "y": votes_percentage})
        context['datapoints'] = json.dumps(datapoints)  # Convert datapoints into a JSON string

        return context
    


"""
Extends ResultsView for displaying poll results to the owner with a different template.
"""
class OwnerResultsView(ResultsView):
    def get_template_names(self):
        return ['polls/owner_results.html']



"""
View for creating a new poll.
"""
class CreatePollView(LoginRequiredMixin, generic.CreateView):
    template_name = "polls/create.html"

    def get(self, request, *args, **kargs):
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet(queryset=Choice.objects.none())
        return render(request, "polls/create.html", 
                      {
                          "question_form": question_form,
                          "choice_formset": choice_formset
                      }
                    )

    def post(self, request, *args, **kargs):
        question_form = QuestionForm(data=self.request.POST)
        choice_formset = ChoiceFormSet(data=self.request.POST)
        # Check if question and choice forms are valid
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save(commit=False)
            # Set publication date, code and owner before saving the question
            question.pub_date = timezone.now()
            question.code = CUID_GENERATOR.generate()  # Generate code
            question.owner = request.user
            question.save()
            question_id = question.id
            choices = choice_formset.save(commit=False)
            # Associate the question ID to each choice before save them
            for choice in choices:
                choice.question_id = question_id
                choice.save()
            return HttpResponseRedirect(reverse('polls:create_confirmation', args=[hashids.encode(question.id)]))
        else:
            return render(request, "polls/create.html", 
                          {
                              "question_form": question_form, 
                              "choice_formset": choice_formset
                          }
                        )



"""
View for displaying the confirmation page after creating a poll.
"""
class ConfirmationView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/create_confirmation.html"
    context_object_name = 'question'

    def get_object(self):
        try:
            encoded_id = self.kwargs.get('encoded_id')
            # Decode the encoded_id using Hashids
            id = hashids.decode(encoded_id)[0]
            # Fetch the student instance by the decoded ID
            question = Question.objects.get(pk=id)
            return question
        except (IndexError, Question.DoesNotExist):
            raise Http404("Question not found")


"""
View to display a list of all polls created by the currently logged-in user.
"""
class UserPollsView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = "polls/user_polls.html"

    def get_queryset(self):
        # Return the questions created by the user
        user_questions = Question.objects.filter(owner=self.request.user,
                                                pub_date__lte=timezone.now()
                                                ).order_by("-pub_date")
        return user_questions
    
    # Add to the context the questions created by the user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_questions = self.get_queryset() # Get the queryset
        context['user_questions'] = user_questions
        return context