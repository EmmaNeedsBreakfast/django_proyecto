from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    classes = ['collapse']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_type', 'price', 'available', 'created_at']
    list_filter = ['category', 'available', 'product_type', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'available']
    
    fieldsets = [
        ('Información Básica', {
            'fields': ['name', 'category', 'product_type', 'price']
        }),
        ('Descripción y Disponibilidad', {
            'fields': ['description', 'available']
        }),
        ('Imagen Principal', {
            'fields': ['image'],
            'classes': ['collapse']
        }),
    ]
    
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_count', 'description_preview']
    search_fields = ['name']
    
    def description_preview(self, obj):
        return obj.description[:50] + '...' if obj.description else 'Sin descripción'
    description_preview.short_description = 'Descripción'
    
    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Productos'

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_preview']
    list_filter = ['product__category']
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover;" />'
        return "Sin imagen"
    image_preview.allow_tags = True
    image_preview.short_description = 'Vista Previa'