from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView

from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'
    
class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy("classroom:thankyou")
    
class TeacherDetailView(DetailView):
    model = Teacher
    
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:teacherlist")
    
class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.all().order_by('firstname')
    context_object_name = 'teachers'
    
class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy("classroom:teacherlist")
    
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    success_url = reverse_lazy("classroom:thankyou")
    
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        return super().form_valid(form)
        