def disapproved_comment(modeladmin, request, queryset):
    queryset.update(approved=False)


def approved_comment(modeladmin, request, queryset):
    queryset.update(approved=True)


disapproved_comment.short_description = 'Reprovar comentarios'
approved_comment.short_description = 'Aprovar comentarios'
