from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from .models import (
			Setting, 
			About, 
			SocialNetwork, 
			TelegramBot, 
			TelegramChatID,
			TelegramChenalID,
			)

# Register your models here.

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
	fieldsets = (
		('Основное', {
			'fields': ('site_title', 'telephone_num', 'email', 'org_name')
			}),
		('Изображения', {
			'fields': ('top_img', 'favicon', 'logo_top',)
			}),
		)

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	def get_urls(self):
		urls = super().get_urls()
		custom_urls = [path('', self.admin_site.admin_view(self.change_view), {'object_id': '1',})]
		return custom_urls + urls

	def response_change(self, request, obj):
		if request.POST.get('_save'):
			return redirect('/admin/')
		return super().response_change(request, obj)

	#@classmethod
	def get_object(self, request, object_id, from_field=None):
		obj, created = Setting.objects.get_or_create(id=object_id)
		return obj
	
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
	list_display = ('name', 'link',)

class TelegramChatIDInLine(admin.TabularInline):
    model = TelegramChatID
    extra = 1

class TelegramChenalIDInLine(admin.TabularInline):
    model = TelegramChenalID
    extra = 1

@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):

	fieldsets = (
		(None, {
			'fields': ('token', )
			}),
		
		)

	inlines = [
		TelegramChatIDInLine,
		TelegramChenalIDInLine,
		]

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	def get_urls(self):
		urls = super().get_urls()
		custom_urls = [path('', self.admin_site.admin_view(self.change_view), {'object_id': ''})]
		return custom_urls + urls

	def response_change(self, request, obj):
		if request.POST.get('_save'):
			return redirect('/admin/')
		return super().response_change(request, obj)
		
	def get_object(self, *args, **kwargs):
		obj, created = TelegramBot.objects.get_or_create(pk=1)
		return obj
