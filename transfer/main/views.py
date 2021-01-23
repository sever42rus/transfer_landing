import telebot
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from services.models import CarouselInner, Services
from settings.models import About, SocialNetwork

# Create your views here.


class Main(View):
    def get(self, request):
        user_agent = request.user_agent
        if user_agent.is_mobile or user_agent.is_tablet:
            template = "main/index_mobile.html"
        else:
            template = "main/index_desktop.html"

        # get setting
        about = About.objects.all()
        social_networks = SocialNetwork.objects.all()
        # get services
        services = Services.objects.all()
        carusels = CarouselInner.objects.all()

        return render(request, template, context={
            'about': about,
            'social_networks': social_networks,
            'services': services,
            'carusels': carusels,
        })

    def post(self, request):
        pass
