from rest_framework import viewsets
from core.models import Category, Saint, Quote
from .serializers import CategorySerializer, SaintSerializer, QuoteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SaintViewSet(viewsets.ModelViewSet):
    queryset = Saint.objects.all()
    serializer_class = SaintSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer