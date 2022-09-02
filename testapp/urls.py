from django.urls import path
from . import views

urlpatterns=[
    path('pocetna', views.pocetna, name="pocetna"),
    path('onama', views.o_nama, name="o_nama"),
    path('pocetna2',views.pocetna2, name="pocetna2"),
]