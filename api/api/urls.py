from django.urls import path, include
from rest_framework import routers

from api.views.proprietario import ProprietarioViewSet
from api.views.inquilino import InquilinoViewSet
from api.views.imovel import ImovelViewSet


router = routers.DefaultRouter()
router.register(r'proprietarios', ProprietarioViewSet)
router.register(r'inquilinos', InquilinoViewSet)
router.register(r'imoveis', ImovelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
