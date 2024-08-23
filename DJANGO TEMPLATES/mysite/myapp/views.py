from django.shortcuts import render

# Create your views here.
def exampleview(request):
    return render(request, 'myapp/example.html')

def variableview(request):
    
    return render(request, 'myapp/variable.html')
