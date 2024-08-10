import random
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import QuestionForm, ChoiceFormSet

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# TODO: Avoid race condition
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



class CreatePollView(generic.CreateView):
    template_name = "polls/create.html"

    def get(self, request, *args, **kargs):
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet(queryset=Choice.objects.none())
        return render(request, "polls/create.html", {"question_form": question_form, "choice_formset": choice_formset})

    def post(self, request, *args, **kargs):
        question_form = QuestionForm(data=self.request.POST)
        choice_formset = ChoiceFormSet(data=self.request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save(commit=False)
            question.pub_date = timezone.now()
            #TODO: prevent repeated code
            question.code = random.randint(11111,99999)
            question.save()
            question_id = question.id
            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.question_id = question_id
                choice.save()
            return HttpResponseRedirect(reverse('polls:confirmation'))
        else:
            return render(request, "polls/create.html", {"question_form": question_form, "choice_formset": choice_formset})

def confirmation(request):
    return render(request, "polls/confirmation.html")

#TODO: prevent double vote and doble question creation on back button hit