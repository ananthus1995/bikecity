from django.db import models

class Bikes(models.Model):
    bikename=models.CharField(max_length=90)
    manufacturer = models.CharField(max_length=90)
    bike_model=models.PositiveIntegerField()
    colour=models.CharField(max_length=55)
    milage=models.FloatField(max_length=55)
    price=models.PositiveIntegerField()






# Create your models here.
