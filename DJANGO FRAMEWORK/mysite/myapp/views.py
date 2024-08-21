from django.http.response import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def simpleview(request):
    return render(request, 'myapp/example.html') #.html
