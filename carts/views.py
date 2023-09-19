from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from carts.models import Cart
from carts.serializer import CartItemSerializer, CartSerializer, CartItemRequestSerializer
from common.logger import module_logger
from products.models import Product

logger = module_logger(__name__)


class CartRemoveView(APIView):
    @extend_schema(responses=CartSerializer)
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        logger.info(f'Removing cart data for product id {product_id}')
        cart = Cart.objects.new_or_get(request)
        for cart_item in cart.cartitem_set.all():
            if cart_item.item.id == product_id:
                cart_item.delete()
        cart_serializer = CartSerializer(instance=cart)
        logger.info(f'Removed cart data for product id {product_id}')
        return Response(cart_serializer.data)


class CartView(GenericAPIView):

    @extend_schema(responses=CartSerializer, request=CartItemRequestSerializer)
    def post(self, request, *args, **kwargs):
        logger.info('Adding to Cart started')
        data = request.data
        logger.debug(f'Data: {data}')
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
                    logger.debug(f'Cart Item Exists in Cart hence updating {cart_item.quantity}')
            if not item_found:
                logger.debug(f'New cart item created')
                serializer.save(user=request.user, cart=cart, item=product, price=product.price)
            cart_serializer = CartSerializer(instance=cart)
            return Response(cart_serializer.data)
