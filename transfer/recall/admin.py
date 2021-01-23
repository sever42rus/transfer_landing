from django.contrib import admin

from .models import Recall, RecallInvite

# Register your models here.


@admin.register(Recall)
class RecallAdmin(admin.ModelAdmin):

    list_display = ('feedback', 'title',
                    'datetime_create', 'datetime_update', )

    fieldsets = (
        (None, {
            'fields': ('feedback', 'title', 'text', 'verified',)
        }),

    )


@admin.register(RecallInvite)
class RecallInviteAdmin(admin.ModelAdmin):

    list_display = ('id', 'feedback', 'done',)

    fieldsets = (
        (None, {
            'fields': ('feedback', 'done',)
        }),

    )
