from django.urls import path
from App1.views import IndexView, AutorView, AutorAPIJson, AutorById

urlpatterns = [
    path('', IndexView),
    path('autor/<int:id>', AutorView),
    path('api/autores-json', AutorAPIJson, name='autores_api'),
    path('api/autor-by-id/<int:id>', AutorById, name='autor_by_id')
]
