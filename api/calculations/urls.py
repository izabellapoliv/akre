from django.urls import path, include
from rest_framework import routers

from calculations.views.contract import ContractViewSet


router = routers.DefaultRouter()
router.register(r'contratos', ContractViewSet, basename='contracts')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='calculations_rest_framework'))
]
