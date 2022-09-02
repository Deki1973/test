from django.urls import path
from . import views

urlpatterns=[
    path('', views.pocetna, name="pocetna"),
    path('/onama', views.o_nama, name="o_nama"),
]