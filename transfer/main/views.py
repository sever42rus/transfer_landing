import telebot
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, View
from services.models import CarouselInner, Services
from settings.models import About, SocialNetwork

# Create your views here.


class MainTemplateViev(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        context['social_networks'] = SocialNetwork.objects.all()
        context['services'] = Services.objects.all()
        context['carusels'] = CarouselInner.objects.all()
        return context

    def get_template_names(self):
        user_agent = self.request.user_agent
        if user_agent.is_mobile or user_agent.is_tablet:
            template_name = "main/index_mobile.html"
        else:
            template_name = "main/index_desktop.html"
        return template_name
