from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView 

# Create your views here.
def index(request):
    numbooks = Book.objects.all().count()
    numinstances = BookInstance.objects.all().count()  
    
    numinstancesavail = BookInstance.objects.filter(status__exact='a').count()
    
    context = {'numbooks':numbooks, 'numinstances':numinstances, 'numinstancesavail':numinstancesavail}
    
    return render(request, 'catalog/index.html', context = context )

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    
class BookDetail(DetailView):
    model = Book
    