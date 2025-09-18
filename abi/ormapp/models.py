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
