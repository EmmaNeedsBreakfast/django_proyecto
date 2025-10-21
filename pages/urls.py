from django.urls import path
from .views import HomeView, MenuView, ServiciosView, ContactoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('servicios/', ServiciosView.as_view(), name='servicios'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
]