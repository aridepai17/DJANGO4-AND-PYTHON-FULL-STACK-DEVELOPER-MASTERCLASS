from django.shortcuts import render, redirect
from . import models
from django.urls import reverse

# Create your views here.
def list(request):
    allcars = models.Car.objects.all()
    context = {'allcars': allcars}
    return render(request, 'cars/list.html', context = context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        #if user submitted new car
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.POST: #delete the car
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('PK not found!')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')