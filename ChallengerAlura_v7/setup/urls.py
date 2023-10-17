from django.contrib import admin
from django.urls import path
from depoimentos.views import CriarDepoimento, DepoimentosAleatorios


urlpatterns = [
    path('admin/', admin.site.urls),
    path('depoimentos/', CriarDepoimento.as_view()),
    path('depoimentos-home/', DepoimentosAleatorios.as_view({'get': 'list'})),
]
