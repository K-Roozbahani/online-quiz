from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404, HttpResponse
from .models import *


def quiz_list_view(request):
    quiz = Quiz.objects.all()
    return render(request, 'quiz-list.html', {'quiz': quiz})


@login_required
def quiz_view(request, pk):
    try:
        quiz = Quiz.objects.prefetch_related('question', 'option').get(pk=pk)


    except Quiz.DoesNotExist:
        return Http404
    return render(request, 'quiz.html', {'quiz': quiz})


def score_view(request):
    if request.method == 'POST':
        answer = Answer(request.POST)
        return HttpResponse(f'Your Score {answer.score}')
    else:
        return Http404
