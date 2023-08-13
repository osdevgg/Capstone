from django.contrib import admin

# Register your models here.
from .models import Booking, Menu

admin.site.register(Menu)
admin.site.register(Booking)

