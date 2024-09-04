#URLS CATALOG

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('CreateBook/', views.BookCreate.as_view(), name = 'CreateBook'),
    path('book/<int:pk>', views.BookDetail.as_view(), name = 'book-detail'),
    path('myview', views.myview, name = 'myview'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('profile/', views.CheckedOutBooksByUserView.as_view(), name = 'profile'),
]