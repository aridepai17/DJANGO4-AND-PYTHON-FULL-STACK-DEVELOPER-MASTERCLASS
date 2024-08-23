from django.shortcuts import render

# Create your views here.
def exampleview(request):
    return render(request, 'myapp/example.html')

def variableview(request):
    
    myvar = {'firstname': 'john', 'lastname': 'skywalker', 'somelist': [1, 2, 3, 4, 5], 'somedict': {'insidekey':'insidevalue'} 
    }
    return render(request, 'myapp/variable.html', context=myvar)
