from django.http.response import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def newsview(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("Page Not Found")

def numpageview(request, numpage):
    topicslist = list(articles.keys()) #['sports', 'finance', 'politics']
    topic = topicslist[numpage]
    
    
    return HttpResponseRedirect(reverse("topicpage", args = [topic]))
        
