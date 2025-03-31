from django.shortcuts import render
from rest_framework import generics, viewsets
from App1.models import AutorModel, FraseModel
from .serializer import AutorModelSerializer, FraseModelSerializer, AutorConFraseSerializer

# Create your views here.
class AutorModelAPIList(generics.ListAPIView):
    queryset = AutorModel.objects.all()
    serializer_class = AutorModelSerializer


class AutorModelAPICreate(generics.CreateAPIView):
    queryset = AutorModel.objects.all()
    serializer_class = AutorModelSerializer


class AutorModelAPIRetrieve(generics.RetrieveAPIView):
    queryset = AutorModel.objects.all()
    serializer_class = AutorModelSerializer


# Los viewsets definen todos los metodos para un modelo de una sola vez
class FraseModelViewSet(viewsets.ModelViewSet):
    queryset = FraseModel.objects.all()
    serializer_class = FraseModelSerializer


class AutorConFraseAPIList(generics.ListAPIView):
    queryset = AutorModel.objects.all()
    serializer_class = AutorConFraseSerializer
