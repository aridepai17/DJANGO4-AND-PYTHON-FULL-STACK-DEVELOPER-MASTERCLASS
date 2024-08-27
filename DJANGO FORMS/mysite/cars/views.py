from django.shortcuts import render, redirect
from django.urls import reverse 
from .forms import ReviewForm

# Create your views here.
def rentalreview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #{'firstname': 'John', 'lastname': 'Doe', 'email': 'X5Qp7@example.com', 'review': 'Great car!'}
            print(form.cleaned_data)
            return redirect(reverse('cars:thankyou'))
    else:
        form = ReviewForm()
    return render(request, 'cars/rentalreview.html', context={'form': form})

def thankyou(request):
    return render(request, 'cars/thankyou.html')