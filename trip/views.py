from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Board, CustomUser, Post, Board_content
from .forms import PostForm, SignUpForm, BoardForm, ContentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import datetime

def signupfunc(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('home')            
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def mypagefunc(request):
    user_id = request.user.id
    object = CustomUser.objects.filter(id__exact = user_id)[0]

    return render(request, 'mypage.html', {'object':object})



@login_required
def homefunc(request):
    object = Post.objects.all()
    return render(request, 'home.html', {'object':object})

@login_required
def createfunc(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        user = request.user.id
        if form.is_valid():
            object = form.save(commit=False)
            # object.user_id = user
            object.save()
            return redirect('detail', pk=object.pk)
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})

@login_required
def detailfunc(request, pk):
    object = Post.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

@login_required
def boardfunc(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.created_date = datetime.datetime.now()
            title.save()
            return redirect('content', pk=title.pk)
    else:
        form = BoardForm()
        object = Board.objects.all()
    return render(request, 'board.html', {'form': form, 'object':object})

@login_required
def contentfunc(request, pk):
    board = Board.objects.get(pk=pk)
    object = Board_content.objects.all()
    if request.method == "POST":
        new = ContentForm(request.POST)
        form = ContentForm()
        if new.is_valid():
            new = new.save(commit=False)
            new.created_date = datetime.datetime.now()
            new.board = board
            new.user = request.user
            new.save()
            print(board)
            return render(request, 'content.html', {'new': new, 'board':board, 'object':object, 'form': form})
    else:
        form = ContentForm()
    return render(request, 'content.html', {'form': form, 'board':board, 'object':object})


def goodfunc(request, pk):
    object = Post.objects.get(pk=pk)
    object.good =  object.good + 1
    object.save()
    return redirect('home')
