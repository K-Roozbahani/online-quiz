from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404, HttpResponse, get_object_or_404
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


def score_view(request, pk):
    if request.method == 'GET':
        score = 0
        answers = Answer.objects.filter(quiz_id=pk).select_related('option', 'question')
        for answer in answers:
            if answer.option.is_true:
                score += answer.question.score
        return HttpResponse(f'Your Score {score}')

    try:
        quiz = Quiz.objects.prefetch_related('question', 'option').get(pk=pk)

    except Quiz.DoesNotExist:
        return Http404
    user = request.user
    score = 0
    for question in quiz.question.all():
        option = request.POST.get(f'{question.number}')
        option = quiz.option.get(id=option)
        answer = Answer.objects.create(user=user, quiz=quiz, option=option,
                                       question=question, is_true=option.is_true)
        if option.is_true:
            score += question.score

    return HttpResponse(f'Your Score {score}')
