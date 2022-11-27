from django.contrib import admin
from .models import *


@admin.register(Quiz)
class QuizAmin(admin.ModelAdmin):
    class Meta:
        model = Quiz


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    class Meta:
        model = Option


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer

# Register your models here.
