from rest_framework import viewsets

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    paginate_by = 5

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    paginate_by = 5

