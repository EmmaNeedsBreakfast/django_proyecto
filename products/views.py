# products/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Category, ProductImage
from django.contrib.auth.mixins import LoginRequiredMixin

# Views que ya teníamos
class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(available=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'

# NUEVAS VIEWS PARA CRUD
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image', 'available', 'product_type']
    success_url = reverse_lazy('products:product_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image', 'available', 'product_type']
    success_url = reverse_lazy('products:product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')