from django.urls import path, include
from rest_framework import routers

from calculations.views.conteudo_segurado import ConteudoSeguradoViewSet
from calculations.views.premio_liquido import PremioLiquidoViewSet
from calculations.views.iof_total import IOFTotalViewSet


router = routers.DefaultRouter()
router.register(r'conteudo-segurado', ConteudoSeguradoViewSet, basename='conteudo_segurado')
router.register(r'premio-liquido', PremioLiquidoViewSet, basename='premio_liquido')
router.register(r'iof-total', IOFTotalViewSet, basename='iof_total')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
