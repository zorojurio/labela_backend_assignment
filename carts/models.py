from django.conf import settings
from django.db import models
from django.db.models import Sum, F

from common.logger import module_logger
from products.models import Product

User = settings.AUTH_USER_MODEL

logger = module_logger(__name__)


class CartManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def new_or_get(self, request):  # getting active cart
        qs = self.get_queryset().filter(user=request.user, active=True)
        if qs.exists() and qs.count() == 1:
            cart_obj = qs.first()
            logger.debug('Cart Exists')
        else:
            cart_obj = Cart.objects.new(user=request.user)
            logger.debug('New Cart Created')
        return cart_obj


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    def get_item_count(self):
        return self.cartitem_set.aggregate(item_count=Sum('quantity'))['item_count'] or 0

    def get_cart_total(self):
        return self.cartitem_set.aggregate(cart_total=Sum(F('price') * F('quantity')))['cart_total'] or 0


class CartItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"cart {str(self.cart.id)} cart-item {self.id} {self.item.title}"

    def get_total_value(self):
        return self.price * self.quantity
