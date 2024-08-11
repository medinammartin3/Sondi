import random
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .forms import CodeForm, QuestionForm, ChoiceFormSet

from .models import Choice, Question

class IndexView(generic.ListView, generic.FormView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    form_class = CodeForm

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        code = self.form.cleaned_data['question_code']
        return reverse_lazy('polls:vote', kwargs={'question_code': code})

    def form_valid(self, form):
        self.form = form
        return super().form_valid(form)
    
# TODO: create updateView for vote
# class VoteView(generic.UpdateView):
#     model = Question
#     template_name = "polls/vote.html"
    
# TODO: Avoid race condition
def vote(request, question_code):
    question = get_object_or_404(Question, code=question_code)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/vote.html",
            {
                "question": question,
                "error_message": "Please select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    



class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



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
            #TODO: prevent repeated question code
            question.code = random.randint(11111,99999)
            question.save()
            question_id = question.id
            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.question_id = question_id
                choice.save()
            return HttpResponseRedirect(reverse('polls:confirmation', args=[question.id]))
        else:
            return render(request, "polls/create.html", {"question_form": question_form, "choice_formset": choice_formset})



class ConfirmationView(generic.DetailView):
    model = Question
    template_name = "polls/confirmation.html"
    context_object_name = 'question'



#TODO: prevent double vote and doble question creation on back button hit