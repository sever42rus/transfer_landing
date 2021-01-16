from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from django.http import HttpResponse

from settings.models import About, SocialNetwork
from services.models import Services, CarouselInner


import telebot
# Create your views here.

class Main(View):
	def get(self, request):
		user_agent = request.user_agent
		if user_agent.is_mobile or user_agent.is_tablet:
			template = "main/index_mobile.html"
		else:
			template = "main/index_desktop.html"

		#get setting
		about = About.objects.all()
		social_networks = SocialNetwork.objects.all()
		#get services
		services = Services.objects.all()
		carusels = CarouselInner.objects.all()

		return render(request, template, context = {
			'about':about, 
			'social_networks':social_networks,
			'services':services, 
			'carusels': carusels,
			})

	def post(self, request):
		pass