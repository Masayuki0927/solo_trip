from django.urls import path
from .views import homefunc, createfunc, detailfunc, signupfunc, loginfunc,\
    logoutfunc, mypagefunc, boardfunc, contentfunc, goodfunc

urlpatterns = [
    path('home/', homefunc, name='home'),
    path('create/', createfunc, name='create'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('signup/', signupfunc, name='signup'),
    path('account/login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('mypage/', mypagefunc, name='mypage'),
    path('board/', boardfunc, name='board'),
    path('content/<int:pk>', contentfunc, name='content'),
    path('good/<int:pk>', goodfunc, name='good'),
]
