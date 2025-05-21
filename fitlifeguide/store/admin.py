from django.contrib import admin
from .models import (
    EquipmentCategory,
    Equipment,
    Cart,
    CartItem,
    Review,
    Order,
    OrderItem
)

@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'category', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'equipment', 'quantity']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['equipment__name', 'user__username', 'comment']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'contact_email']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'equipment', 'quantity', 'price_at_purchase']
