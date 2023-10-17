from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from depoimentos.models import Depoimento
from depoimentos.serializer import DepoimentoSerializer

class ViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_criar_depoimento(self):
        data = {
            "foto": "caminho/para/foto.jpg",
            "Depoimento": "Este é um depoimento de teste.",
            "nome": "John Doe"
        }
        url = reverse('nome_da_url_para_criar_depoimento')  # Substitua 'nome_da_url_para_criar_depoimento' pela URL correta

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Depoimento.objects.count(), 1)
        depoimento = Depoimento.objects.get()
        self.assertEqual(depoimento.foto, data['foto'])
        self.assertEqual(depoimento.Depoimento, data['Depoimento'])
        self.assertEqual(depoimento.nome, data['nome'])

    def test_depoimentos_aleatorios(self):
        self.client = APIClient()
        url = reverse('nome_da_url_para_depoimentos_aleatorios')  # Substitua 'nome_da_url_para_depoimentos_aleatorios' pela URL correta

        # Crie alguns depoimentos de teste no banco de dados
        Depoimento.objects.create(foto="foto1.jpg", Depoimento="Depoimento 1", nome="Alice")
        Depoimento.objects.create(foto="foto2.jpg", Depoimento="Depoimento 2", nome="Bob")
        Depoimento.objects.create(foto="foto3.jpg", Depoimento="Depoimento 3", nome="Charlie")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Certifique-se de que este valor corresponda ao número de depoimentos no resultado
