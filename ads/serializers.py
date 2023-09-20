from rest_framework import serializers

from ads.models import Car, Apartment


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'title', 'description', 'price', 'country_id', 'category_id', 'image', 'mobile', 'user_id')


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('id', 'id_apartment', 'value', 'latitude', 'longtitude')
