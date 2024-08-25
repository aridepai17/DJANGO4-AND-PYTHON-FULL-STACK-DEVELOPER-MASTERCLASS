from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        
        return f"{self.firstname} {self.lastname} {self.age}"