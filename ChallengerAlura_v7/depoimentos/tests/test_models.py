from django.test import TestCase
from depoimentos.models import Depoimento

class DepoimentoModelTest(TestCase):
    def setUp(self):
        # Criar um objeto de teste para o modelo
        self.depoimento = Depoimento(
            foto='caminho/para/foto.jpg',
            Depoimento='Este é um depoimento de teste.',
            nome='John Doe'
        )

    def test_str_method(self):
        # Verificar se o método __str__ retorna o nome corretamente
        self.assertEqual(str(self.depoimento), 'John Doe')

    def test_depoimento_model(self):
        # Salvar o objeto no banco de dados
        self.depoimento.save()

        # Buscar o objeto do banco de dados
        depoimento_no_banco = Depoimento.objects.get(pk=self.depoimento.pk)

        # Verificar se os campos são iguais
        self.assertEqual(depoimento_no_banco.foto, 'caminho/para/foto.jpg')
        self.assertEqual(depoimento_no_banco.Depoimento, 'Este é um depoimento de teste.')
        self.assertEqual(depoimento_no_banco.nome, 'John Doe')
