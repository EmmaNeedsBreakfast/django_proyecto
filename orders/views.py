# orders/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        return Order.objects.all().order_by('-created_at')

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/order_form.html'
    fields = ['customer_name', 'customer_phone', 'customer_address', 'notes', 'delivery_time']
    success_url = reverse_lazy('orders:order_list')
    
    def form_valid(self, form):
        # Aquí luego agregarás la lógica para los items del pedido
        return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'orders/order_form.html'
    fields = ['customer_name', 'customer_phone', 'customer_address', 'status', 'notes', 'delivery_time']
    success_url = reverse_lazy('orders:order_list')

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    success_url = reverse_lazy('orders:order_list')