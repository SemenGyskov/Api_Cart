from rest_framework import generics
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer

class ProductListCreateView(generics.ListCreateAPIView): # для чтения (по GET-запросу) и создания списка данных (по POST-запросу)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): #чтение, изменение и добавление отдельной записи (GET-, PUT-, PATCH- и DELETE-запросы).
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartListCreateView(generics.ListCreateAPIView): # для чтения (по GET-запросу) и создания списка данных (по POST-запросу)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): #чтение, изменение и добавление отдельной записи (GET-, PUT-, PATCH- и DELETE-запросы).
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
