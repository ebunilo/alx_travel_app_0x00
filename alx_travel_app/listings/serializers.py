from rest_framework import serializers
from .models import Listing, ListingImage

class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ['id', 'image', 'caption', 'is_primary']

class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, read_only=True)
    host_name = serializers.CharField(source='host.get_full_name', read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price', 'property_type',
            'bedrooms', 'bathrooms', 'location', 'latitude', 'longitude',
            'is_available', 'created_at', 'updated_at', 'host', 'host_name', 'images'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'host_name']