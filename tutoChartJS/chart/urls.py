from django.urls import path
from chart import views

urlpatterns = [
    path('', views.home, name='home_page'),
    
]