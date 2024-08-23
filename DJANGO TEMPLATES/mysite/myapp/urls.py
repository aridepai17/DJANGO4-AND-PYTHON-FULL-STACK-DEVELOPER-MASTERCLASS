from django.urls import path
from . import views

appname = 'myapp'

urlpatterns = [
    path('', views.exampleview, name = 'example'),
    path('variable/', views.variableview, name = 'variable'),
]