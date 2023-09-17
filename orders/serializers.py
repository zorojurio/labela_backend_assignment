from rest_framework import serializers

from orders.models import Order, OrderItem
from products.serializer import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    order_item_total = serializers.SerializerMethodField(read_only=True)
    item = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'item',
            'price',
            'quantity',
            'order_item_total'
        ]

    def get_order_item_total(self, obj: OrderItem):
        return obj.get_total_value()


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(read_only=True, many=True)
    total_order_value = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = [
            'order_id',
            'total_order_value',
            'orderitem_set',
            'delivery_date'
        ]

    def get_total_order_value(self, obj: Order):
        return obj.get_total_order_value()


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_date']
