from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listone/', views.listone),
    path('listall/', views.listall),
]