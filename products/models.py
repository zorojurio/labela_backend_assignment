from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=20,
        blank=True,
        null=True
    )
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
