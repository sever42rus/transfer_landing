from django.contrib import admin

from .models import Comment, Feedback

# Register your models here.


class CommentFeedbackInLine(admin.TabularInline):
    model = Comment
    extra = 1
    fieldsets = (
                ('None',
                 {'fields': ('comment', )},
                 ),
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'telephone',
                    'datetime_create', 'datetime_update', )
    list_filter = ('datetime_create', 'datetime_update',
                   'in_work', 'performed', )
    search_fields = ['name', 'email', 'telephone']
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'telephone', 'message',)
        }),
        ('Выполнение', {
            'fields': ('in_work', 'performed',),
        }),
    )

    inlines = [CommentFeedbackInLine]
