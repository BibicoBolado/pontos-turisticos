from rest_framework.serializers import ModelSerializer
from pontos.models import Atracoes
#TENHO QUE IMPORTAR O MODEL PONTOS PARA PODER
#TER ACESSO AOS SEUS OBJETOS E DEFINIR OS CAMPOS QUE EU QUERO SERIALIZAR

class AtracoesSerializer(ModelSerializer):
    class Meta:
        model=Atracoes
        fields=('id','nome','descricao','horario_funcionamento','idade_minima','foto')
