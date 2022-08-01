from django.urls import path, include
from rest_framework import routers

from api.views.proprietario import ProprietarioViewSet
from api.views.inquilino import InquilinoViewSet


router = routers.DefaultRouter()
router.register(r'proprietarios', ProprietarioViewSet)
router.register(r'inquilinos', InquilinoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
