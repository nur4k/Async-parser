from django.contrib import admin

from ads.models import Car, Apartment


admin.site.register((Car, Apartment))
