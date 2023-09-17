from django.contrib import admin

from orders.models import OrderItem, Order


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem


class CartAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

    class Meta:
        model = Order


admin.site.register(Order, CartAdmin)
admin.site.register(OrderItem)
