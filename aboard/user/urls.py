from django.urls import path
from django.shortcuts import redirect
from user.views import login_page, logout_page, register


urlpatterns = [
    path("login/", login_page, name="user_login"),
    path("regist/", register, name="user_regist"),
    path("logout/", logout_page, name="user_logout"),
]