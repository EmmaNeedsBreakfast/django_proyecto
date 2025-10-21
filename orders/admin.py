from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ['subtotal']
    
    def subtotal(self, obj):
        return f"Bs. {obj.quantity * obj.price}"
    subtotal.short_description = 'Subtotal'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_phone', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer_name', 'customer_phone', 'customer_address']
    list_editable = ['status']  # Cambiar estado directo desde la lista
    readonly_fields = ['created_at', 'total_amount']
    
    # Campos organizados en secciones
    fieldsets = [
        ('Información del Cliente', {
            'fields': ['customer_name', 'customer_phone', 'customer_address']
        }),
        ('Información del Pedido', {
            'fields': ['total_amount', 'status', 'delivery_time', 'notes']
        }),
        ('Metadata', {
            'fields': ['created_at'],
            'classes': ['collapse']
        }),
    ]
    
    inlines = [OrderItemInline]
    
    # Acciones personalizadas
    actions = ['mark_as_confirmed', 'mark_as_delivered']
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} pedidos marcados como confirmados.')
    mark_as_confirmed.short_description = "Marcar pedidos seleccionados como CONFIRMADOS"
    
    def mark_as_delivered(self, request, queryset):
        updated = queryset.update(status='delivered')
        self.message_user(request, f'{updated} pedidos marcados como entregados.')
    mark_as_delivered.short_description = "Marcar pedidos seleccionados como ENTREGADOS"

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'subtotal']
    list_filter = ['order__status']
    search_fields = ['product__name', 'order__customer_name']
    
    def subtotal(self, obj):
        return f"Bs. {obj.quantity * obj.price}"
    subtotal.short_description = 'Subtotal'

# Registrar los modelos
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)