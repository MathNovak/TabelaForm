from django.db import models

class Tabela(models.Model):

    nome = models.CharField(verbose_name='Nome', max_length=50)
    cep = models.CharField(verbose_name='CEP', max_length=9)
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)
    cidade = models.CharField(verbose_name='Cidade', max_length=30)
    uf = models.CharField(verbose_name='UF', max_length=2)
    telefone = models.CharField(verbose_name='Telefone', max_length=20)

    def __str__(self):
        return f'{self.nome} - {self.endereco}'

