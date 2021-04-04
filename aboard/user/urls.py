from django.urls import path
from django.shortcuts import redirect
from user.views import login_page, logout_page, register, edit
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/", login_page, name="user_login"),
    path("regist/", register, name="user_regist"),
    path("logout/", logout_page, name="user_logout"),
    path("edit/", edit, name="user_edit"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)