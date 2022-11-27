from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Q, Manager


class Quiz(models.Model):
    title = models.CharField(max_length=50, default='Quiz')


class Question(models.Model):
    number = models.SmallIntegerField()
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    score = models.IntegerField(default=1)

    class Meta:
        unique_together = ('number', 'quiz')

    def __str__(self):
        return '(' + str(self.number) + ') ' + str(self.description)


class Option(models.Model):
    name = models.CharField(max_length=2)
    question = models.ForeignKey(Question, related_name='option', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='option', on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    is_true = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'question', 'description')

    def __str__(self):
        return '(' + str(self.name) + ')  ' + str(self.description)


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='answer', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='answers', on_delete=models.CASCADE)
    submit_date = models.DateTimeField(auto_now_add=True)

    @property
    def score(self):
        true_option = Q(is_true=True, answer=self)
        question = Question.objects.filter(option=true_option).annotate(sum_score=Sum('score'))
        return question[0].sum_score