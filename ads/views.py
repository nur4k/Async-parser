import json
from django.http import HttpResponse
import httpx
import asyncio

from  rest_framework import generics

from ads.models import Car, Apartment
from ads.serializers import CarSerializer, ApartmentSerializer

from core import script


class CarView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    


class ApartmentView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


def parse_and_save_data(request):
    script.process_rent_kv()
    script.process_buy_kv()
    script.process_auto()
    return HttpResponse("Данные успешно спарсены и сохранены в базе данных.")