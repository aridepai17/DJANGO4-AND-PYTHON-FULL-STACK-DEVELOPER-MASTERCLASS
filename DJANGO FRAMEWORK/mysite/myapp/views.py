from django.http.response import HttpResponse

def homeview(request):
    return HttpResponse("Home Page")