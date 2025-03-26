from django.shortcuts import render
from rest_framework import generics
from App1.models import AutorModel
from .serializer import AutorModelSerializer

# Create your views here.
class AutorModelAPIList(generics.ListAPIView):
    queryset = AutorModel.objects.all()
    serializer_class = AutorModelSerializer