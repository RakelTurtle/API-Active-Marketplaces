from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MarketplaceSerializer

from .models import Marketplace


class MarketplaceAPIView(APIView):
    """
    API Marketplaces Turtle Brand Protection
    """

    def get(self, request):
        api = Marketplace.objects.all()
        serializer = MarketplaceSerializer(api, many=True)
        return Response(serializer.data)

        

