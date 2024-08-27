from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100) #pk
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.brand} {self.year}"
    