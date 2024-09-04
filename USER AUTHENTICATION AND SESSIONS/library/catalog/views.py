from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView, ListView 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 

# Create your views here.
def index(request):
    numbooks = Book.objects.all().count()
    numinstances = BookInstance.objects.all().count()  
    
    numinstancesavail = BookInstance.objects.filter(status__exact='a').count()
    
    context = {'numbooks':numbooks, 'numinstances':numinstances, 'numinstancesavail':numinstancesavail}
    
    return render(request, 'catalog/index.html', context = context )

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    
class BookDetail(DetailView):
    model = Book
    
@login_required
def myview(request):
    return render(request, 'catalog/myview.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'
    
class CheckedOutBooksByUserView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user)