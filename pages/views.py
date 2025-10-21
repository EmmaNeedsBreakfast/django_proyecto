# pages/views.py
from django.views.generic import TemplateView
from products.models import Product, Category

class HomeView(TemplateView):
    template_name = 'home.html'

class MenuView(TemplateView):
    template_name = 'menu.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ServicesView(TemplateView):
    template_name = 'services.html'