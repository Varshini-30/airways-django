from django.db import models

# Create your models here.


class Airway(models.Model):
    city = (('oneway', 'oneway'), ('roundtrip', 'roundtrip'),
            ('multicity', 'multicity'))
    From = models.CharField(max_length=200)
    To = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    Deperature_date = models.IntegerField()
    Return = models.IntegerField()
    Bookingclass = models.CharField(max_length=100)
    Traveler = models.IntegerField()
    price = models.IntegerField()


class log(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
