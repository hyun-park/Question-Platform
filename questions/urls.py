from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('upvote/<int:question_id>', views.upvote_question, name='upvote_question'),
    path('downvote/<int:question_id>', views.downvote_question, name='downvote_question'),
]
