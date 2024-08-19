from django.urls import path
from . import views

urlpatterns = [
    path('SimpleViews', views.simpleview)
]