from django import forms
from .models import Chat, Post, Board, Board_content, Chat, Room
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_image','area',)

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', )

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', )

class ContentForm(forms.ModelForm):

    class Meta:
        model = Board_content
        fields = ('text', )

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('text', )