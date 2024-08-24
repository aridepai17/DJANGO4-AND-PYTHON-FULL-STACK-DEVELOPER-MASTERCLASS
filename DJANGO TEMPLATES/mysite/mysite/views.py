from django.shortcuts import render

def mycustompagenotfoundview(request, exception):
    
    return render(request, '404.html', status=404)