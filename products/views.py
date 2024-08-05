from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer

# Create your views here.


class ProductCreateAPIView(generics.CreateAPIView):
    """
    API view to create a new product.

    This view handles the POST request to create a new product entry in the database.
    It uses the ProductSerializer to validate and save the product data.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ API view to update an existing product."""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    """API view to retrieve a specific product's details."""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    """API view to delete a specific product."""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

