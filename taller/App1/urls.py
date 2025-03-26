from django.urls import path
from App1.views import IndexView, AutorView

urlpatterns = [
    path('', IndexView),
    path('autor/<int:id>', AutorView)
]
