from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            default=timezone.now)

    def isLiked(self, user_id):
        try:
            user_quetion_upvote = self.upvotes.get(user_id=user_id)
            return True
        except ObjectDoesNotExist:
            return False

    def __str__(self):
        return self.text


class Upvote(models.Model):
    question = models.ForeignKey(Question, related_name='upvotes', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.user.username