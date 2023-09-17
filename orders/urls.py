from django.urls import path

from orders.views import OrderCreateAPIView

urlpatterns = [
    path('checkout', OrderCreateAPIView.as_view())
]
