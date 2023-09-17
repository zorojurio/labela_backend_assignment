from django.urls import path

from products.views import ProductViewSet, ProductOverview
from rest_framework import renderers

product_list = ProductViewSet.as_view({
    'get': 'list'
})
product_create = ProductViewSet.as_view({
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
})
product_update = ProductViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
})
product_delete = ProductViewSet.as_view({
    'delete': 'destroy'
})

urlpatterns = [
    path('', product_list, name='product-detail'),
    path('overview/', ProductOverview.as_view(), name='product-overview'),
    path('create/', product_create, name='product-create'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('<int:pk>/update/', product_update, name='product-update'),
    path('<int:pk>/delete', product_delete, name='product-delete'),
]