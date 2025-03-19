from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def IndexView(request):
    '''Esto es la página principal'''
    return HttpResponse("Holis molis")