from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('rentalreview/', views.rentalreview, name = 'rentalreview'),
    path('thankyou/', views.thankyou, name = 'thankyou'),
]

