from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Board, CustomUser, Message, Post, Board_content, Follow
from .forms import PostForm, SignUpForm, BoardForm, ContentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q
import pandas as pd
import requests

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
def profilefunc(request, username):
    object = CustomUser.objects.filter(username__exact = username)[0]
    follower_count = object.do_follow_user.all().count()
    followerd_count = object.accept_follow_user.all().count()
    if username == request.user.username:
        return render(request, 'mypage.html', {'object':object, 'follower_count':follower_count, 'followerd_count':followerd_count})
    else:
        user = request.user
        for item in user.do_follow_user.all():
            if username == item.followerd.username:
                follow = True
                for followitem in object.do_follow_user.all():
                    if followitem.followerd == request.user:
                        followed = True
                        return render(request, 'profile.html', {'object':object, 'follow':follow, 'followed':followed, 'follower_count':follower_count,'followerd_count':followerd_count})
                return render(request, 'profile.html', {'object':object, 'follow':follow, 'follower_count':follower_count,'followerd_count':followerd_count})
        follow = False
    return render(request, 'profile.html', {'object':object, 'follow':follow, 'follower_count':follower_count, 'followerd_count':followerd_count})


def homefunc(request):
    object = Post.objects.all()
    # keyword = request.GET.get('keyword')
    # if keyword:
    #     object = object.filter(
    #              Q(title__icontains=keyword) | Q(content__icontains=keyword)
    #            )
    return render(request, 'home.html', {'object':object})


def searchfunc(request):
    print('test')
    object = Post.objects.all()
    keyword = request.GET.get('keyword')
    if keyword:
        object = object.filter(
                 Q(title__icontains=keyword) | Q(content__icontains=keyword)
               )
    return render(request, 'search.html', {'object':object})


@login_required
def createfunc(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        user = request.user
        if form.is_valid():
            object = form.save(commit=False)
            print(object.post_image)
            # object.post_image = request.FILES['post_image']
            object.person = user
            object.created_date = datetime.datetime.now()
            object.save()
            return redirect('detail', pk=object.pk)
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})

@login_required
def detailfunc(request, pk):
    object = Post.objects.get(pk=pk)

    # REQUEST_URL = "https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426"
    # APP_ID = "1089286695599073385"
    # params = {
    # "format":"json",
    # "largeClassCode":"japan",
    # "middleClassCode":"okinawa",
    # "smallClassCode":"nahashi",
    # "applicationId":APP_ID
    # }  
    # content = requests.get(REQUEST_URL, params).json()
    # df = pd.DataFrame({'hotelName': [],'reviewAverage': [],'hotelInformationUrl': []},index=[])
    # index=1
    # for item in content['hotels']:
    #     df.loc[index] = [
    #                 item['hotel'][0]['hotelBasicInfo']['hotelName'],
    #                 item['hotel'][0]['hotelBasicInfo']['reviewAverage'],
    #                 item['hotel'][0]['hotelBasicInfo']['hotelInformationUrl']
    #                 ]
    #     index = index + 1
    # hotels = df.sort_values('reviewAverage', ascending=False).head(5)
    return render(request, 'detail.html', {'object':object})



@login_required
def boardfunc(request):
    object = Board.objects.all()
    keyword = request.GET.get('keyword')
    if keyword:
        object = object.filter(title__icontains=keyword)
    return render(request, 'board.html', {'object':object})


@login_required
def create_boardfunc(request):
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
    return render(request, 'create_board.html', {'form': form, 'object':object})


@login_required
def contentfunc(request, pk):
    object = Board_content.objects.all()
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        print("post")
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
        print("get")
    return render(request, 'content.html', {'form': form, 'object':object ,'board':board})

@login_required
def goodfunc(request, pk):
    object = Post.objects.get(pk=pk)
    object.good =  object.good + 1
    object.save()
    return redirect('home')

@login_required
def followfunc(request, username):
    alluser = CustomUser.objects.all()
    object = Follow(follower=request.user, followerd=alluser.filter(username = username)[0])
    object.save()
    return redirect('profile', username = username)
    
@login_required
def unfollowfunc(request, username):
    alluser = CustomUser.objects.all()
    object = Follow.objects.filter(follower = request.user, followerd = alluser.filter(username = username)[0])[0].delete()
    return redirect('profile', username = username)

@login_required
def messagefunc(request, username):
    alluser = CustomUser.objects.all()
    object =  Message.objects.filter(Q(user_from = request.user, user_to = alluser.filter(username = username)[0]) \
        | Q(user_to = request.user, user_from = alluser.filter(username = username)[0]))
    return render(request, 'message.html', {'object':object})    
