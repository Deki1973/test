from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pocetna(request):
    return HttpResponse("OVO JE POCETNA STRANICA")

def o_nama(request):
    return HttpResponse("OVO JE PRICA O NAMA")

def pocetna2(request):
    ime="Dean"
    return render(request, 'pocetna2.html', {'ime':ime,})

