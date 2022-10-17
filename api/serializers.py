from dataclasses import fields
from rest_framework import serializers

from .models import Marketplace


class MarketplaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marketplace

        fields = (
            'id',
            'name',
            'active'
        )