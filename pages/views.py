from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class MenuView(TemplateView):
    template_name = 'menu.html'

class ServiciosView(TemplateView):
    template_name = 'servicios.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'
