from django.contrib import admin
from .models import Comment
from .actions import disapproved_comment, approved_comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'approved']
    actions = [disapproved_comment, approved_comment]


admin.site.register(Comment, CommentAdmin)
