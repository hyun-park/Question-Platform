from django.contrib import admin
from .models import Question, Upvote

admin.site.register(Question)
admin.site.register(Upvote)