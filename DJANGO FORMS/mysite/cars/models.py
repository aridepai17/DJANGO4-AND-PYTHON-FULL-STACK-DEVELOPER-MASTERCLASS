from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    stars = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])