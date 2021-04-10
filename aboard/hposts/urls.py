from django.urls import path, reverse
from django.shortcuts import redirect
from hposts import views as hposts




urlpatterns = [
    # path("", hposts.hposts_page, name="hposts_page"),
    path("", hposts.AllBlogs.as_view(), name="hposts_page"),
    path("<int:pk>/", hposts.OneBlog.as_view(), name="hposts_page"),
    path("comments/add/<int:post_id>/", hposts.add_comment, name="post_comment"),
    path('new/', hposts.PostCreateView.as_view(), name='post_new'),
    path('edit/<int:pk>/', hposts.PostUpdateView.as_view(), name='post_edit'),

    # path("comments/add/com/<int:post_id>/", hposts.view_comment, name="post_comment"),

    # re_path(r'^add$', hposts.add, name='add'),
]