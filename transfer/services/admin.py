from django.contrib import admin

from .models import CarouselInner, Services

# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ['image_pictogram', ]

    list_display = ('title', 'image_pictogram',)

    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'full_description')
        }),
        ('Пиктограмма', {
            'fields': (('pictogram', 'image_pictogram'),)
        }),

    )


@admin.register(CarouselInner)
class CarouselInnerAdmin(admin.ModelAdmin):
    readonly_fields = ['image_img', ]

    list_display = ('title', 'image_img',)

    fieldsets = (
        (None, {
            'fields': ('service', 'title', 'text', )
        }),
        ('Изображение', {
            'fields': (('img', 'image_img'),)
        }),

    )
