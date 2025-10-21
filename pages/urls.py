# pages/urls.py
from django.urls import path
from .views import HomeView, MenuView, AboutView, ContactView, ServicesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServicesView.as_view(), name='services'),
]