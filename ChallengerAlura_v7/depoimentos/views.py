from rest_framework import viewsets, status, generics
from django.http import JsonResponse
from rest_framework.response import Response
from depoimentos.models import Depoimento
from depoimentos.serializer import  DepoimentoSerializer
import random

class CriarDepoimento(generics.ListCreateAPIView):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

class DepoimentosAleatorios(viewsets.ModelViewSet):
    serializer_class = DepoimentoSerializer

    def get_queryset(request):

        depoimentos = Depoimento.objects.all()

        if len(depoimentos) >= 3:
            depoimentos_aleatorios = random.sample(list(depoimentos), 3)
            return  depoimentos_aleatorios
        else:
            return depoimentos    