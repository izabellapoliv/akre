from django.contrib import admin

from api.models.proprietario import Proprietario
from api.models.inquilino import Inquilino
from api.models.imovel import Imovel

# Register your models here.
admin.site.register(Proprietario)
admin.site.register(Inquilino)
admin.site.register(Imovel)
