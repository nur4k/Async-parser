from django.db import models


class Car(models.Model):
    title = models.CharField('Название', max_length=155)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length=155)
    country_id = models.IntegerField()
    category_id = models.IntegerField()
    image = models.ImageField(upload_to='media/auto')
    mobile = models.CharField('Телефон', max_length=15)
    user_id = models.CharField('Юзэр', max_length=155)

    def __str__(self):
        return self.user_id

class Apartment(models.Model):
    id_apartment = models.CharField('id', max_length=155)
    value = models.CharField('Значение', max_length=155)
    latitude = models.CharField('Широта', max_length=155)
    longtitude = models.CharField('Долгота', max_length=155)
