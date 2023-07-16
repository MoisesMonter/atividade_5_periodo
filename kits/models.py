from django.db import models
from django import forms

class Kit(models.Model):
    codigo = models.CharField(max_length=100)
    preco = models.FloatField()

class Telhado(models.Model):
    telhado = models.CharField(max_length=100)
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)

class Modulo(models.Model):
    conexao = models.CharField(max_length=100)
    quant_modulos = models.IntegerField()
    modelo_modulo = models.CharField(max_length=100)
    potencia_wp_unitaria_modulo = models.CharField(max_length=100)
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)

class Inversor(models.Model):
    overload_maximo = models.CharField(max_length=100)
    kwp = models.CharField(max_length=100)
    qtde_inversor_1 = models.IntegerField()
    inversor_1 = models.CharField(max_length=100)
    qtde_inversor_2 = models.IntegerField()
    inversor_2 = models.CharField(max_length=100)
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)

class Cabo(models.Model):
    quant_cabo_vermelho = models.IntegerField()
    modelo_cabo_vermelho = models.CharField(max_length=100)
    quant_cabo_preto = models.IntegerField()
    modelo_cabo_preto = models.CharField(max_length=100)
    quant_pares_conectores = models.IntegerField()
    modelo_par_conector = models.CharField(max_length=100)
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)

class StringBox(models.Model):
    quant_stringbox = models.IntegerField()
    modelo_stringbox = models.CharField(max_length=100)
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)

class Estrutura(models.Model):
    quant_estrutura_1 = models.IntegerField()
    modelo_estrutura_1 = models.CharField(max_length=100)
    quant_estrutura_2 = models.IntegerField()
    modelo_estrutura_2 = models.CharField(max_length=100)
    quant_estrutura_3 = models.IntegerField()
    modelo_estrutura_3 = models.CharField(max_length=100)
    quant_estrutura_4 = models.IntegerField()
    modelo_estrutura_4 = models.CharField(max_length=100)
    quant_estrutura_5 = models.IntegerField()
    modelo_estrutura_5 = models.CharField(max_length=100)
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)

class Marca(models.Model):
    marca_inversor = models.CharField(max_length=100)
    marca_modulo = models.CharField(max_length=100)
    coluna1 = models.IntegerField()
    kit = models.OneToOneField(Kit, on_delete=models.CASCADE)


class ExcelUploadForm(forms.Form):
    file = forms.FileField()