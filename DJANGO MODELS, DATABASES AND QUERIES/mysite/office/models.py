from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60, validators = [MinValueValidator(1), MaxValueValidator(300)])
    
    def __str__(self):
        
        return f"{self.firstname} {self.lastname} {self.age}"