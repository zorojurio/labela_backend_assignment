import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum, F

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

    def __str__(self):
        return f"Order Item: {self.item.title} {self.id}"

    def get_total_value(self):
        return self.price * self.quantity


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    delivery_date = models.DateTimeField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.order_id}"

    def get_total_order_value(self):
        return self.orderitem_set.aggregate(order_total=Sum(F('price')*F('quantity')))['order_total'] or 0
