from django.urls import path

from .views import MarketplaceAPIView


urlpatterns = [
    path('marketplaces/', MarketplaceAPIView.as_view(), name='marketplaces'),
]