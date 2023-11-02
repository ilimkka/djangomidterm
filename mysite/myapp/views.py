from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.utils import timezone

from .models import Choice, Question, Answer
from .forms import QuestionForm, AnswerForm

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {"latest_question_list": latest_question_list}
    return render(request, "myapp/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.order_by("-pub_date")
    return render(request, "myapp/detail.html", {"question": question, 'answers': answers})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "myapp/results.html", {"question": question})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
    else:
        form = QuestionForm()

    return render(request, 'myapp/add_question.html', {'form': form})

def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
    else:
        form = QuestionForm(instance=question)

    return render(request, 'myapp/update_question.html', {'form': form})

def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question.delete()
    return redirect('../../')

def add_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.pub_date = timezone.now()
            answer.save()
            return redirect('../')

    else:
        form = AnswerForm()

    return render(request, 'myapp/add_answer.html', {'form': form, 'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "myapp/detail.html",
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
        return HttpResponseRedirect(reverse("myapp:results", args=(question.id,)))