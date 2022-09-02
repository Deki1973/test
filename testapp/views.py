from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pocetna(request):
    return HttpResponse("OVO JE POCETNA STRANICA")
