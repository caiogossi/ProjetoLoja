from django.db import models


# Create your models here.

class Vendedor(models.Model):
    cpf_vendedor = models.IntegerField(primary_key=True)
    nome_vendedor = models.CharField(max_length=30, null=False)
    data_admissao = models.DateField(auto_now=True)
    salario_bruto = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    salario_liquido = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    percentual_comissao = models.DecimalField(max_digits=3, decimal_places=2)
    quantidade_vendas = models.IntegerField(null=False)

class Venda(models.Model):
    num_venda = models.IntegerField(primary_key=True,serialize=True)
