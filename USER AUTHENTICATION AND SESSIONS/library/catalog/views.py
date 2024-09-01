from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre, Language

# Create your views here.
def index(request):
    numbooks = Book.objects.all().count()
    numinstances = BookInstance.objects.all().count()  
    
    numinstancesavail = BookInstance.objects.filter(status__exact='a').count()
    
    context = {'numbooks':numbooks, 'numinstances':numinstances, 'numinstancesavail':numinstancesavail}
    return render(request, 'index.html', context = context )