from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from hposts.models import Blog, Tags
from hposts.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages




class AllBlogs(ListView):
    model = Blog
    template_name = "posts.html"
    paginate_by = 3

    def get_queryset(self):
        if self.request.GET.get("tag"):
            return self.model.objects.filter(tags__name=self.request.GET.get("tag"))
        return super().get_queryset()

    

 
    

class OneBlog(DetailView):
    model = Blog
    template_name = "singlposts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

# def post_detail(request, slug):
#     template_name = "post_detail.html"
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True).order_by("-created_on")
#     new_comment = None
#     # Comment posted
#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(
#         request,
#         template_name,
#         {
#             "post": post,
#             "comments": comments,
#             "new_comment": new_comment,
#             "comment_form": comment_form,
#         },
#     )


def add_comment(request, post_id):
    '''
    обработка добавления коментария в базу
    '''
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save(post_id)
            messages.info(request, 'Ваш коментарий успешно отправлен')
            messages.info(request, 'После проверки модератором он будет доступен на сайте')
        else:
            messages.info(request, 'Ошибка добавления коментария')
            messages.info(request, 'Проверьте введенные данные')
    return HttpResponseRedirect(reverse("hposts_page", args=(post_id, )))
