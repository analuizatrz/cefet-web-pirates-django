from django.db import models

# Create your models here.
class Tesouro(models.Model):
    nome = models.CharField(max_length=45)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    img_tesouro = models.ImageField(upload_to="imgs")

    def __str__(self):
        return "{nome}, {quantidade} R$ {preco}".format(nome=self.nome, quantidade=self.quantidade, preco=self.preco)