from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AutorModelAPIList,
    AutorModelAPICreate,
    AutorModelAPIRetrieve,
    FraseModelViewSet,
    AutorConFraseAPIList
)

router = DefaultRouter()
router.register('frases', FraseModelViewSet, basename='frases')

urlpatterns = [
    path('autores-list/', AutorModelAPIList.as_view(), name='autores_list'),
    path('autores-frases/', AutorConFraseAPIList.as_view(), name='autor_frase'),
    path('autores-create/', AutorModelAPICreate.as_view(), name='autores_create'),
    path('autores-retrieve/<int:pk>', AutorModelAPIRetrieve.as_view(), name='autores_retrieve'),
]

urlpatterns += router.urls
