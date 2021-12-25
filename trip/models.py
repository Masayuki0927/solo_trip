from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField

class CustomUser(AbstractUser):
	age = models.CharField(max_length=10)

class Follow(models.Model):
    follower = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'do_follow_user', blank=True, null=True)
    followerd = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'accept_follow_user' , blank=True, null=True) 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    person = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, default=None, blank=True, null=True)
    good = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Board(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Board_content(models.Model):
    text = TextField()
    created_date = models.DateTimeField()
    user = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, default=None, blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=None, blank=True, null=True)

class Message(models.Model):
    text = TextField()
    created_date = models.DateTimeField()
    user_from = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'message_from', blank=True, null=True)
    user_to = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'message_to' , blank=True, null=True) 