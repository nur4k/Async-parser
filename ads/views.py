from  rest_framework import generics

from ads.models import Car, Apartment
from ads.serializers import CarSerializer, ApartmentSerializer


class CarView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ApartmentView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
