from django.urls import path, reverse
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from hposts import views as hposts




urlpatterns = [
    path("", hposts.AllBlogs.as_view(), name="hposts_page"),
    path("<int:pk>/", hposts.OneBlog.as_view(), name="hposts_page"),
    path("comments/add/<int:post_id>/", hposts.add_comment, name="post_comment"),
    path('new/', hposts.PostCreateView.as_view(), name='post_new'),
    path('edit/<int:pk>/', hposts.PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', hposts.PostDeleteView.as_view(), name='post_delete'),
    path('comments/<int:pk>/', hposts.new_single, name="new_single"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)