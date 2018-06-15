from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracoes
from .serializers import AtracoesSerializer

class AtracoesViewset(ModelViewSet):
    queryset=Atracoes.objects.all()
    serializer_class=AtracoesSerializer
    filter_fields = ('nome', 'descricao')