from rest_framework.response import Response
from rest_framework.views import APIView

from carts.models import Cart
from orders.models import OrderItem
from orders.serializers import OrderCreateSerializer, OrderSerializer


# Create your views here.
class OrderCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = OrderCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            cart = Cart.objects.new_or_get(request)
            cart_item_qs = cart.cartitem_set.all()
            if cart_item_qs.exists():
                order = serializer.save(user=request.user, cart=cart)
                print(serializer.validated_data)

                for cart_item in cart.cartitem_set.all():
                    cart_item.active = False
                    OrderItem.objects.create(
                        order=order,
                        item=cart_item.item,
                        cart_item=cart_item,
                        price=cart_item.price,
                        quantity=cart_item.quantity
                    )
                    cart_item.save()
                cart.active = False
                cart.save()
                order_serializer = OrderSerializer(instance=order)
                return Response(order_serializer.data)
            return Response({'message': 'Empty Cart'})

