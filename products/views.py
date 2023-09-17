from rest_framework import viewsets

from common.mixins import StaffEditorPermissionMixin
from products.models import Product
from products.serializer import ProductSerializer


class ProductViewSet(StaffEditorPermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
