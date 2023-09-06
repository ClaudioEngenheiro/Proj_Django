from django.db import models

# Create your models here.

class Topicos(models.Model):
    name = models.CharField(max_length=264,unique=True)
    
    def __str__(self):
        return self.name
    
class Paginas(models.Model):
    topico = models.ForeignKey(Topicos,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class RegistroAcesso(models.Model):
    name = models.ForeignKey(Paginas,on_delete=models.CASCADE)
    date = models.DateField
    hora = models.TimeField((""), auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.date)    

class Produto(models.Model):
    nome = models.CharField(max_length=256)
    data_venc = models.DateField()
    fornecedor = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    
