from django.urls import path
from .views import quiz_list_view, quiz_view

urlpatterns = [
    path('', quiz_list_view, name='quiz_list_view'),
    path('quiz/<int:pk>/', quiz_view, name='quiz_view'),
]
