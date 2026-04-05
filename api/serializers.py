from rest_framework import serializers
from core.models import Category, Saint, Quote

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saint
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'