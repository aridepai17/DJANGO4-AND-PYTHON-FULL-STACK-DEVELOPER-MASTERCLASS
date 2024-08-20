from django.urls import path
from . import views

urlpatterns = [
    path('<int:numpage>/', views.numpageview),
    path('<str:topic>/', views.newsview, name = "topicpage"),
]