from django.db import models

class Depoimento(models.Model):
    foto = models.ImageField(upload_to='depoimentos_fotos/')
    Depoimento = models.TextField()
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome