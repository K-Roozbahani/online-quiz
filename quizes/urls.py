from django.urls import path
from .views import quiz_list_view, quiz_view, score_view

urlpatterns = [
    path('', quiz_list_view, name='quiz_list_view'),
    path('quiz/<int:pk>/', quiz_view, name='quiz_view'),
    path('quiz/<int:pk>/score/', score_view, name='show_score'),
]
