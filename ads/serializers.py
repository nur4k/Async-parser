from rest_framework import serializers

from ads.models import Car, Apartment
from ads.services import fetch_data


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'title', 'description', 'price', 'country_id', 'category_id', 'image', 'mobile', 'user_id')

    async def create(cls, validated_data):
        url = 'https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=40&category_id=1502'
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "device": "pc"
        }
        data = await fetch_data(url, headers)

        count = 0
        for item in data['items']:
            car = Car(
                title=item['title'],
                description=item['description'],
                price=item['price'],
                country_id=item['country_id'],
                category_id=item['category_id'],
                image=item['image'],
                mobile=item['mobile'],
                user_id=item['user_id']
            )
            car.save()  
            count += 1
            if count == 20:
                break
        
        return car  


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('id', 'id_apartment', 'value', 'latitude', 'longtitude')
