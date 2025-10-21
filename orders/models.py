from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('preparing', 'En preparación'),
        ('delivering', 'En camino'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ]
    
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Agregué default
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Te sugiero agregar esto
    delivery_time = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.customer_name}"
    
    def get_total(self):
        """Por si quieres calcular el total dinámicamente también"""
        return sum(item.subtotal() for item in self.orderitem_set.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Agregué related_name
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def subtotal(self):
        return self.quantity * self.price