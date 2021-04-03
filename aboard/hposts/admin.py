from django.contrib import admin
from hposts.models import Blog, Tags, Comment


class AdminBlog(admin.ModelAdmin):
    list_display = ["title", "user"]


class AdminTags(admin.ModelAdmin):
    list_display = ["name", "id"]

# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    


admin.site.register(Blog, AdminBlog)
admin.site.register(Tags, AdminTags)
admin.site.register(Comment, CommentAdmin)