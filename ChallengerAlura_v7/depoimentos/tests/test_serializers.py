from django.test import TestCase
from depoimentos.models import Depoimento
from depoimentos.serializer import DepoimentoSerializer

class DepoimentoSerializerTest(TestCase):
    def test_serializer_valido(self):
        data = {
            "foto": "caminho/para/foto.jpg",
            "Depoimento": "Este é um depoimento de teste.",
            "nome": "John Doe"
        }
        serializer = DepoimentoSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_campos_validos(self):
        data = {
            "foto": "caminho/para/foto.jpg",
            "Depoimento": "Este é um depoimento de teste.",
            "nome": "John Doe"
        }
        serializer = DepoimentoSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["foto"], "caminho/para/foto.jpg")
        self.assertEqual(serializer.validated_data["Depoimento"], "Este é um depoimento de teste.")
        self.assertEqual(serializer.validated_data["nome"], "John Doe")

    def test_serializer_invalido(self):
        data = {
            "foto": "caminho/para/foto.jpg",
            "Depoimento": "",  # Depoimento em branco, o que deve ser inválido
            "nome": "John Doe"
        }
        serializer = DepoimentoSerializer(data=data)
        self.assertFalse(serializer.is_valid())