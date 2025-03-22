from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Product, Recommendation
from .serializers import ProductSerializer, RecommendationSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RecommendationListView(generics.ListAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

