from django.contrib import admin
from .models import Comment
from .actions import aprova_comentarios, reprova_comentarios


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'approved']
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comment, CommentAdmin)
