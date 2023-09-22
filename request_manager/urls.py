from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, RequestViewSet

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
