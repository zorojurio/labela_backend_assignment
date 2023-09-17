from django.conf import settings
from django.db import models

from carts.models import CartItem, Cart
from products.models import Product

User = settings.AUTH_USER_MODEL


# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_item = models.OneToOneField(CartItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    line_item_cost = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.00)
    line_item_total_cost = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order Item: {self.item.title} {self.id}"


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)  # AB31DE3
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.order_id
