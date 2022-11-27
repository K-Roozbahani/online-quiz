from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Q


class Quiz(models.Model):
    title = models.CharField(max_length=50, default='Quiz')


class Question(models.Model):
    number = models.SmallIntegerField()
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    score = models.IntegerField(default=1)

    class Meta:
        unique_together = ('number', 'quiz')


class Option(models.Model):
    name = models.CharField(max_length=2)
    question = models.ForeignKey(Question, related_name='option', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='option', on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    is_true = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'question', 'description')


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    option = models.ManyToManyField(Option, related_name='answer', blank=True)

    @property
    def score(self):
        true_option = Q(is_true=True, answer=self)
        question = Question.objects.filter(option=true_option).annotate(sum_score=Sum('score'))
        return question[0].sum_score
