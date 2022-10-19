from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework import filters

class ProductViewset(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
