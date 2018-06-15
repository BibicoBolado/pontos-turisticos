from rest_framework.serializers import ModelSerializer
from pontos.models import Pontos
from rest_framework.fields import SerializerMethodField
#TENHO QUE IMPORTAR O MODEL PONTOS PARA PODER
#TER ACESSO AOS SEUS OBJETOS E DEFINIR OS CAMPOS QUE EU QUERO SERIALIZAR
from atracoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontosSerializer(ModelSerializer):
    atracoes=AtracoesSerializer(many=True  ) #many = True usa quando for relação m2m
    comentario=ComentarioSerializer(many=True)
    avaliacao=AvaliacaoSerializer(many=True)
    des_completa=SerializerMethodField() #preciso criar isso aqui para criar o metodo dentro do serialzier
    class Meta:
        model = Pontos
        fields = ('id','nome', 'descricao','status','foto',
            'atracoes','comentario','avaliacao','des_completa',
            'des_completa2'
        )

    def get_des_completa(self,obj): #objeto é o proprio serializer
        return '%s - %s' %(obj.nome, obj.descricao)