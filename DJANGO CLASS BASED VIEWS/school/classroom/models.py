from django.db import models

# Create your models here.
class Teacher(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} teaches {self.subject}"