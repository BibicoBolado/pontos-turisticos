from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao
# Create your models here.

class Pontos(models.Model):
    nome=models.CharField('Nome',max_length=150)
    descricao=models.TextField()
    status=models.BooleanField('Aprovado',default=False)
    atracoes=models.ManyToManyField(Atracoes,null=True,blank=True)
    comentario=models.ManyToManyField(Comentario,null=True,blank=True)
    avaliacao=models.ManyToManyField(Avaliacao,null=True,blank=True)
    localizcao=models.OneToOneField(Localizacao,on_delete=models.CASCADE,null=True,blank=True)
    foto=models.ImageField(upload_to='pontos_turisticos',null=True,blank=True)
    #upload_to é o local onde as fotos serás salvas dentro da pasta raiz de imagem
    @property
    def des_completa2(self):
        return '%s - %s' %(self.nome,self.descricao)

    def __str__(self):
        return self.nome