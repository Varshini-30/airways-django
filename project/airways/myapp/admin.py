from django.contrib import admin
from .models import Airway
# Register your models here.

# admin.site.register(Airway)


class Airwayadmin(admin.ModelAdmin):
    list_display = ('id', 'From', 'To', 'image', 'Deperature_date',
                    'Return', 'Bookingclass', 'Traveler', 'price')


admin.site.register(Airway, Airwayadmin)
