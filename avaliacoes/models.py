from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avaliacao(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    comentario=models.TextField(null=True,blank=True)
    escolhas=(
        (1,'Ótima'),
        (2,'Boa'),
        (3,'Regular'),
        (4,'Ruim'),
        (5,'Péssima'),
    )
    nota=models.IntegerField('Nota',choices=escolhas)
    data=models.DateTimeField(auto_now_add=True)

    def __str__():
        return self.user.username