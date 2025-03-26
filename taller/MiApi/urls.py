from django.urls import path
from .views import (
    AutorModelAPIList
)

urlpatterns = [
    path('autores-list/', AutorModelAPIList.as_view(), name='autores_list'),
]