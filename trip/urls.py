from django.urls import path
from .views import homefunc, createfunc, detailfunc, signupfunc, loginfunc,\
    logoutfunc, boardfunc, contentfunc, goodfunc, profilefunc, followfunc, unfollowfunc, \
    roomfunc, searchfunc, create_boardfunc, chatfunc,create_roomfunc, followuserfunc, followeduserfunc, \
    deletefunc, updatefunc, tmpfunc

urlpatterns = [
    path('home/', homefunc, name='home'),
    path('create/', createfunc, name='create'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('signup/', signupfunc, name='signup'),
    path('account/login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('profile/<username>', profilefunc, name='profile'),
    path('board/', boardfunc, name='board'),
    path('create_board/', create_boardfunc, name='create_board'),
    path('content/<int:pk>', contentfunc, name='content'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('follow/<username>', followfunc, name='follow'),
    path('unfollow/<username>', unfollowfunc, name='unfollow'),
    path('room/', roomfunc, name='room'),
    path('search/', searchfunc, name='search'),
    path('create_room/', create_roomfunc, name='create_room'),
    path('chat/<room_id>', chatfunc, name='chat'),
    path('followuser/<username>', followuserfunc, name='followuser'),
    path('followeduser/<username>', followeduserfunc, name='followeduser'),
    path('update/<int:pk>', updatefunc, name='update'),
    path('delete/<int:pk>', deletefunc, name='delete'),
    path('tmp/<int:pk>', tmpfunc, name='tmp'),
    # path('recommend/', recommendfunc, name='recommend'),
]
