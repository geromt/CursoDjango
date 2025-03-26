from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AutorModel, FraseModel
from django.core.serializers import serialize


# Create your views here.
def IndexView(request):
    '''Esto es la página principal'''

    objeto = AutorModel.objects.all().order_by("id")

    return render(request, "index.html", {"objeto":objeto})


def AutorView(request, id):
    autor = get_object_or_404(AutorModel, id=id)
    return render(request, "autor.html", {"objeto": autor})

# Vistas API


def AutorAPIJson(request):
    autores = AutorModel.objects.all().order_by("id")
    autores_serialize = serialize('json', autores)
    return HttpResponse(autores_serialize, content_type='application/json', status=200)

def  AutorById(request, id):
    autor = AutorModel.objects.filter(id=id)
    print("Holi ", autor)
    autor_serialize = serialize('json', autor)
    return HttpResponse(autor_serialize, content_type='application/json', status=200)