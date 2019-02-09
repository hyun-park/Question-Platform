from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Question, Upvote
from .forms import QuestionForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Count

@login_required
def question_list(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.created_date = timezone.now()
            question.updated_date = timezone.now()
            question.save()
            return redirect('question_list')
        else:
            return redirect('question_list')
    else:
        questions = Question.objects.annotate(upvote_counts=Count('upvotes')).order_by('-upvote_counts', '-created_date')
        user_id = request.user.id
        for question in questions:
            question.isLiked = question.isLiked(user_id)
        form = QuestionForm()
    return render(request, 'questions/question_list.html',
                  {'questions': questions,
                   'form': form,
                   })

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.username = username
            user.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def upvote_question(request, question_id):
    if request.method == "POST":
        try:
            Upvote.objects.get(question_id=question_id, user=request.user)
            messages.success(request, f'한 질문에는 하나의 좋아요만 표시할 수 있습니다!')
        except MultipleObjectsReturned:
            messages.success(request, f'한 질문에는 하나의 좋아요만 표시할 수 있습니다!')
        except Upvote.DoesNotExist:
            upvote = Upvote(question=Question.objects.get(id=question_id), user=request.user)
            upvote.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required
def downvote_question(request, question_id):
    if request.method == "POST":
        try:
            upvote = Upvote.objects.get(question_id=question_id, user=request.user)
            upvote.delete()
        except Upvote.DoesNotExist:
            return redirect('/')
        return redirect('/')
    else:
        return redirect('/')

