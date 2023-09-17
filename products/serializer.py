from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductOverviewSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'overview'
        ]


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'title',
            'overview',
            'price',
            'active',
            'slug',
            'timestamp',
            'updated'
        ]
