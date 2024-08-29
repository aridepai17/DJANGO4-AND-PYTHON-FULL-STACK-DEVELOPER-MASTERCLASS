from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from classroom.models import Teacher

from classroom.forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    templatename = 'classroom/home.html'
    
class ThankYouView(TemplateView):
    templatename = 'classroom/thankyou.html'
    
class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy("classroom:thankyou")
    
class TeacherDetailView(DetailView):
    model = Teacher
    
class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.all().order_by('firstname')
    context_object_name = 'teachers'
    
class ContactView(FormView):
    formclass = ContactForm
    templatename = 'classroom/contact.html'
    
    success_url = reverse_lazy("classroom:thankyou")
    
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        return super().form_valid(form)
        