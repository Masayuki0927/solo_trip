from django.urls import path
from .views import homefunc, createfunc, detailfunc, signupfunc, loginfunc,\
    logoutfunc, boardfunc, contentfunc, goodfunc, profilefunc, followfunc, unfollowfunc, \
    messagefunc

urlpatterns = [
    path('home/', homefunc, name='home'),
    path('create/', createfunc, name='create'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('signup/', signupfunc, name='signup'),
    path('account/login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('profile/<username>', profilefunc, name='profile'),
    path('board/', boardfunc, name='board'),
    path('content/<int:pk>', contentfunc, name='content'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('follow/<username>', followfunc, name='follow'),
    path('unfollow/<username>', unfollowfunc, name='unfollow'),
    path('message/<username>', messagefunc, name='message'),
]
