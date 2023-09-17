from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from carts.models import Cart
from carts.serializer import CartItemSerializer, CartSerializer
from products.models import Product


class CartRemoveView(APIView):
    def get(self, request, *args, **kwargs):
        print(request)
        product_id = kwargs.get('pk')
        cart = Cart.objects.new_or_get(request)
        for cart_item in cart.cartitem_set.all():
            if cart_item.item.id == product_id:
                cart_item.delete()
        cart_serializer = CartSerializer(instance=cart)
        return Response(cart_serializer.data)


class CartView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        product_id = data.get('item')
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = get_object_or_404(Product, pk=product_id)
            cart = Cart.objects.new_or_get(request)
            item_found = False
            for cart_item in cart.cartitem_set.all():
                if cart_item.item.id == product_id:
                    cart_item.quantity = serializer.validated_data.get('quantity')
                    cart_item.price = product.price
                    cart_item.save()
                    item_found = True
            if not item_found:
                serializer.save(user=request.user, cart=cart, item=product, price=product.price)
            cart_serializer = CartSerializer(instance=cart)
            return Response(cart_serializer.data)
