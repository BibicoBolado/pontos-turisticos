from django.db import models

# Create your models here.

class Atracoes(models.Model):
    nome=models.CharField('Nome',max_length=150)
    descricao=models.TextField()
    horario_funcionamento=models.TextField()
    idade_minima=models.IntegerField()
    foto=models.ImageField(upload_to='atracoes',null=True,blank=True)


    def __str__(self):
        return self.nome