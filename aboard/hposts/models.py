from django.db import models
from user.models import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Record title.",
    )
    create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Create date.",
    )
    text = models.TextField(
        verbose_name="Record content.",
    )
    user = models.ForeignKey(
        User,
        related_name="blogs",
        verbose_name="User.",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        "Tags",
        blank=True,
        verbose_name="#hashtag",
        related_name="hashtags",
    )

    photo = models.ImageField(
        "Изображение",
        upload_to="media/",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "blogs"
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("-create", "-id")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hposts_page", kwargs ={'pk': self.pk})


class Tags(models.Model):
    name = models.CharField(
        max_length=15,
        verbose_name="#hashtag",
        # unique=True,
    )

    class Meta:
        db_table = "tags"
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ("name",)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments",
    )
    # title = models.CharField(
    #     max_length=100,
    #     default='',
    #     verbose_name='Заголовок коментария'
    # )
    name = models.CharField(
        max_length=50,
        verbose_name="User name.",
    )
    email = models.EmailField(
        max_length=50,
        verbose_name="User email.",
    )
    body = models.TextField(
        max_length=256,
        verbose_name="Content."
    )
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(
        blank=True,
        default=False
        )


    class Meta:
        db_table = 'comments'
        ordering = ['created_on', ]
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return '{}'.format(self.body)















# class Comment(models.Model):

#     email = models.EmailField(
#         verbose_name="Commentator email.",
#     )
#     comment = models.TextField(
#         verbose_name="Content.",
#     )
#     user = models.ForeignKey(
#         User,
#         related_name="comments",
#         verbose_name="User.",
#         on_delete=models.CASCADE,
#     )
#     create = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Created.",
#     )
#     is_moderated = models.BooleanField(
#         default=False,
#         verbose_name="Is modetated.",
#     )

#     def __str__(self):
#         return self.user
