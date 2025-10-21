# products/models.py
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    # Si quieres el tipo específico de charcutería:
    PRODUCT_TYPES = [
        ('embutido', 'Embutido'),
        ('queso', 'Queso'),
        ('fiambre', 'Fiambre'),
        ('bebida', 'Bebida'),
        ('tablita', 'Tablita'),
        ('panini', 'Panini'),
        ('otros', 'Otros'),
    ]
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='otros')
    
    def __str__(self):
        return f"{self.name} - Bs.{self.price}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='products/gallery/')
    
    def __str__(self):
        return f"Imagen de {self.product.name}"