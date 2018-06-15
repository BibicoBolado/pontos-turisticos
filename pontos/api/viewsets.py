from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
#TENHO QUE IMPORTAR O MEU MODELVIEWSET
from pontos.models import Pontos
#TENHO QUE IMPORTAR O MODEL PONTOS PARA PODER
#TER ACESSO AOS SEUS OBJETOS
from .serializers import PontosSerializer
#PRECISO DAR ESSE IMPORT PARA CHAMALO EM
#SERIALIZER_CLASS


class PontosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    #queryset = Pontos.objects.all() #COMENTEI PARA PODER USAR O MÉTODO DEF_QUERYSET
    #PEGA OS DADOS DO MEU MODEL ATRAVÉS DO MANAGER OBJETC
    serializer_class = PontosSerializer
    #INDICA COMO VOCê IRÁ MOSTRAR OS DADOS E QUAIS CAMPOS
    #IRÃO PARA O JSON ESSE VALOR APONTA PARA A CLASSE
    #SERIALIZER QUE EU CRIAR NO MEU SERIALIZERS.PY




#    lookup_prefixes = {
#        '^': 'istartswith',
#        '=': 'iexact',
#        '@': 'search',
#        '$': 'iregex',
#    }
#o lookup é usado como visto em nome





    filter_backends = (SearchFilter,)
    #permission_classes=(IsAuthenticated,) #Tipo de autorização, esse tipo aqui só ve se o cara ta logado!
    #authentication_classes=(TokenAuthentication,)
    search_fields = ('nome', 'descricao','localizcao__linha1')
    #localizcao é uma foreignkey, a sintaxes para buscar por um campo da foreignker é o nome dela seguido de __ e um campo qualquer
    lookup_field = 'id' #MUDA O URI do meu endpoint
    #O LOOKUP FIELD DEVE SER UNICO DENTRO DO MEU BD

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = Pontos.objects.all()

        if id:
            queryset = Pontos.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset #devido a buscar ser lazy loading ele só acessa o banco de dados aqui!






#######################Rescrevendo o CRUD padrão##########################
    def list(self, request, *args, **kwargs):
        return super(PontosViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontosViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontosViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontosViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontosViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontosViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'],detail=True) #DETAIL=TRUE SIGNFICA QUE APONTA PARA UM RECURSO ESPECIFICO E NÃO PARA O ENDPOINT COMO UM TODO.
    def denunciar(self,request,id=None):#ele recebe um pk por isso tem um detail na linha de cima
        return Response('SE FUDEU OTARIO!!!')

    @action(methods=['get'], detail=False) #DETAIL= FALSE faz com que eu pegue um endpoint sem a URI
    def teste(self, request):
        pass