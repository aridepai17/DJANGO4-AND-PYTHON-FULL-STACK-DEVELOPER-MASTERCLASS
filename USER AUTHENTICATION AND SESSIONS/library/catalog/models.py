from django.db import models
from django.db.models import TextField
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        
        return reverse('book-detail', kwargs={'pk':self.pk})
    
class Author(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dateofbirth = models.DateField(null = True, blank = True)
    
    class Meta:
        ordering = ['firstname', 'lastname']
        
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self):
        return f'{self.id} ({self.book.title})'
    