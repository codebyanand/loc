from rest_framework import serializers
from .models import Category, Saint, Quote, Resource, Favorite
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SaintSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    quote_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Saint
        fields = '__all__'
    
    def get_quote_count(self, obj):
        return obj.quotes.count()

class QuoteSerializer(serializers.ModelSerializer):
    saint = SaintSerializer(read_only=True)
    saint_id = serializers.PrimaryKeyRelatedField(
        queryset=Saint.objects.all(), source='saint', write_only=True
    )
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='categories', many=True, write_only=True, required=False
    )
    
    class Meta:
        model = Quote
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    tags_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Resource
        fields = '__all__'
    
    def get_tags_list(self, obj):
        return obj.get_tags_list()

class FavoriteSerializer(serializers.ModelSerializer):
    quote_detail = QuoteSerializer(source='quote', read_only=True)
    saint_detail = SaintSerializer(source='saint', read_only=True)
    resource_detail = ResourceSerializer(source='resource', read_only=True)
    
    class Meta:
        model = Favorite
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']