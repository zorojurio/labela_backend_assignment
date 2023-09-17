from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    def get_item_count(self):
        item_count = 0
        for cart_item in self.cartitem_set.all():
            item_count += cart_item.quantity
        return item_count


class CartItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    line_item_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"cart {str(self.cart.id)} cart-item {self.id} {self.item.title}"
