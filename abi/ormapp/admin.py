from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('cid', 'brand', 'model_name', 'year', 'price', 'horsepower', 'rating')

admin.site.register(Car, CarAdmin)
