# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r'categories', views.CategoryViewSet)
# router.register(r'saints', views.SaintViewSet)
# router.register(r'quotes', views.QuoteViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'saints', views.SaintViewSet)
router.register(r'quotes', views.QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]