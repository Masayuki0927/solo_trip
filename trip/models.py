from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField
import uuid

class CustomUser(AbstractUser):
	age = models.CharField(max_length=10)

class Follow(models.Model):
    follower = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'do_follow_user', blank=True, null=True)
    followerd = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'accept_follow_user' , blank=True, null=True) 

class Post(models.Model):
    area_spot = (
        ('hokkaido', '北海道'),
        ('okinawa', '沖縄'),
        ('東北', '東北'),
        ('関東', '関東'),
        ('東海', '東海'),
        ('北陸', '北陸'),
        ('近畿', '近畿'),
        ('山陽・山陰', '山陽・山陰'),
        ('四国', '四国'),
        ('海外', '海外'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    person = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, default=None, blank=True, null=True)
    good = models.IntegerField(default=0)
    post_image = models.ImageField(upload_to = 'post/', blank=True, null=True, default='model/sea.jpeg')
    created_date = models.DateTimeField()
    area = models.CharField(max_length=100 ,choices=area_spot, default=None,blank=True, null=True)


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

    def __str__(self):
        return self.text

class Room(models.Model):
    user_from = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'message_from', blank=True, null=True)
    user_to = models.ForeignKey(get_user_model( ), on_delete=models.CASCADE, related_name = 'message_to' , blank=True, null=True) 
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.user_to.username


class Chat(models.Model):
    text = TextField()
    created_date = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None, blank=True, null=True)
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.text
