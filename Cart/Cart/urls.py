from django.urls import path
from api.views import ProductListCreateView, ProductRetrieveUpdateDestroyView, CartListCreateView, CartRetrieveUpdateDestroyView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-destroy'),
]