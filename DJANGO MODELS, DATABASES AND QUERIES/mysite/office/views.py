from django.shortcuts import render
from . import models

# Create your views here.
def listpatients(request):
    allpatients = models.Patient.objects.all()
    context = {'patients':allpatients}
    return render(request, 'office/list.html', context = context)