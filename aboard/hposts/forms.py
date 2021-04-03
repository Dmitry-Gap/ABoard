from django.forms import ModelForm
from django import forms
from hposts.models import Comment, Blog


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def save(self, post_id):
        self.instance.post=Blog.objects.get(id=post_id)
        return super().save()
        



