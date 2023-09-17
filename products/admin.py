from django.contrib import admin

from products.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', ]


admin.site.register(Product, ProductAdmin)
