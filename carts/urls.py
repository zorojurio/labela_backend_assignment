from django.urls import path

from carts.views import CartView, CartRemoveView

urlpatterns = [
    path('', CartView.as_view()),
    path('<int:pk>/', CartRemoveView.as_view())
]
