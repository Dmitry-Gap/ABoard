from django.urls import path
from home import views as home

urlpatterns = [
    path("", home.home_page, name="home_page"),
    # path("about/", home.about_page, name="about_page"),
    path("contact/", home.contact_page, name="contact_page"),
    path("post/", home.post_page, name="post_page"),
    # path("login/", home.login_page, name="login_page")

]