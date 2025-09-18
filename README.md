# Ex02 Django ORM Web Application
## Date: 18.09.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('cid', 'brand', 'model_name', 'year', 'price', 'horsepower', 'rating')

admin.site.register(Car, CarAdmin)

models.py

from django.db import models

class Car(models.Model):
    cid = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    horsepower = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.year})"

```


## OUTPUT
![alt text](<Screenshot (6).png>)

## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
