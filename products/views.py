from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from common.mixins import StaffEditorPermissionMixin
from products.models import Product
from products.serializer import ProductSerializer, ProductOverviewSerializer


class ProductViewSet(StaffEditorPermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductOverview(APIView):
    def get(self, request, *args, **kwargs):
        products_qs = Product.objects.all()
        product_data = ProductOverviewSerializer(instance=products_qs, many=True)
        return Response(product_data.data)