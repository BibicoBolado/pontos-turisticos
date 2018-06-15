"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers #importando os routers
from django.conf import settings
from django.conf.urls.static import static
from pontos.api.viewsets import PontosViewSet
from atracoes.api.viewsets import AtracoesViewset
from avaliacoes.api.viewsets import AvaliacaoViewset
from comentarios.api.viewsets import ComentarioViewset
from localizacao.api.viewsets import LocalizacaoViewset
from rest_framework.authtoken.views import obtain_auth_token


#http://www.django-rest-framework.org/tutorial/quickstart/
#GUIA PARA COMEÇAR COM ESSES ROUTERS
router = routers.DefaultRouter()
router.register(r'pontoturistico', PontosViewSet,base_name='Pontos')
#preciso colocar o base_name porque eu tirei o queryset do viewset então
#o viewset não sabe a qual model ele está associado, por isso coloco   o
#base_name com o nome do model que a viewset está associada.
router.register(r'atracoes', AtracoesViewset)
router.register(r'avaliacao', AvaliacaoViewset)
router.register(r'comentarios', ComentarioViewset)
router.register(r'localizacao', LocalizacaoViewset)
# O PRIMEIRO VALOR RETORNADO É O RECURSO DA MINHA URL e O SEGUNDO
#É A VIEWSET QUE VAI RECEVER ESSA ROTA IDENTIFICADA

urlpatterns = [
    path('',include(router.urls)), #INCLUI MEU ROUTER (ROTAS) NA URL RAIZ
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
