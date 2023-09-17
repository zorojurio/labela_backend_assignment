from rest_framework import serializers

from carts.models import CartItem, Cart


class CartListCartItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartItem
        fields = [
            'cart',
            'item',
            'price',
            'quantity',
            'total'
        ]

    def get_total(self, obj: CartItem):
        return obj.get_total_value()


class CartSerializer(serializers.ModelSerializer):
    cartitem_set = CartListCartItemSerializer(read_only=True, many=True)
    total = serializers.SerializerMethodField(read_only=True)
    count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'cartitem_set',
            'total',
            'count'
        ]

    def get_total(self, obj: Cart):
        return obj.get_cart_total()

    def get_count(self, obj: Cart):
        return obj.get_item_count()


class CartItemSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = CartItem
        fields = [
            'item',
            'quantity'
        ]