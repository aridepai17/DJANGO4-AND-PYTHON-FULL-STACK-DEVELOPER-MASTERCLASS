from django.urls import path
from . import views

urlpatterns = [
    path('', views.exampleview),
    path('variable/', views.variableview)
]