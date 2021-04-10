from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from hposts.models import Blog, Tags, Comment
from hposts.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string
from django.template.context_processors import csrf



class AllBlogs(ListView):
    model = Blog
    template_name = "posts.html"
    paginate_by = 10

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
    


# class OneCom(DetailView):
#     model = Comment
#     template_name = "comments.html"

#     def get_context_data(self, **kwargs):
#         contexts = super().get_context_data(**kwargs)
#         contexts["comment_form"] = CommentForm()
#         return contexts

# def view_comment(request, post_id, body):
#     template_name = "comments.html"
#     post = get_object_or_404(Comment, post_id=post_id)
#     comments = Comment.objects.filter(active=True).order_by("-created_on")
#     if comment_forms.is_valid():
#         new_comment.post = post
#         new_comment.save()
#         # return render(request, {'user_form': user_form } 
#     else:
#         comment_forms = CommentForm()

#     return render(
#         request,
#         template_name,
#         {
#             "body": body,
#             "comments": comments,
#             # "new_comment": new_comment,
#             "comment_forms": comment_forms,
#         },
#     )
   



def view_comment(request, active, post_id):
    '''
    добавление на страницу списка добавленных комментариев
    '''
    all_comments = Comment.objects.filter(
        active=True
    )
    data = {
        'comments_form': False,
        'all_comments': all_comments
    }
    if add(request):
        comments_forms = CommentsForm(initial={
            'post': post(request)
        })
        data['comments_form'] = comments_forms
    data.update(csrf(request))
    return render('comments.html', data)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title','text', 'tags']
    template_name = 'post_edit.html'
    login_url = "user_login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title','text']
    template_name = 'post_create.html'
    login_url = "user_login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False    
    # def get_absolute_url(self):
    #     return HttpResponseRedirect(reverse("hposts_page", args=(post_id, )))

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False