from django.db import models

# Create your models here.

class Booking(models.Model):
#    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
#    no_of_guests = models.DecimalField(max_digits=6, decimal_places=0)
    no_of_guests = models.SmallIntegerField()
    bookingdate = models.DateTimeField()

class Menu(models.Model):
#    id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)
#    inventory = models.IntegerField(max_length=5)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return  f'{self.title} : {str(self.price)}'

