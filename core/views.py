from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    """Simple homepage view"""
    return JsonResponse({
        'message': 'Welcome to Lives of Christ API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'api_saints': '/api/saints/',
            'api_categories': '/api/categories/',
            'api_quotes': '/api/quotes/',
        }
    })

@api_view(['GET'])
def api_root(request):
    """API root endpoint"""
    return Response({
        'message': 'Lives of Christ API',
        'version': '1.0.0',
        'endpoints': {
            'saints': '/api/saints/',
            'categories': '/api/categories/',
            'quotes': '/api/quotes/',
        }
    })