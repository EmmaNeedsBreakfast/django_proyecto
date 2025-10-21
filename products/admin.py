from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Número de forms vacíos para agregar imágenes
    classes = ['collapse']  # Para que sea colapsable

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created_at']
    list_filter = ['category', 'available', 'product_type', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'available']  # Puedes editar directo en la lista
    prepopulated_fields = {'slug': ('name',)}  # Si agregas slug field después
    
    # Campos organizados en secciones
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
    
    inlines = [ProductImageInline]  # Galería de imágenes
    
    # Para mostrar miniaturas en el admin (opcional)
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover;" />'
        return "Sin imagen"
    image_preview.allow_tags = True
    image_preview.short_description = 'Vista Previa'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description_preview']
    search_fields = ['name']
    
    def description_preview(self, obj):
        return obj.description[:50] + '...' if obj.description else 'Sin descripción'
    description_preview.short_description = 'Descripción'

# Registrar los modelos
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)