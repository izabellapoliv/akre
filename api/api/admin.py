from django.contrib import admin

from api.models.proprietario import Proprietario
from api.models.inquilino import Inquilino

# Register your models here.
admin.site.register(Proprietario)
admin.site.register(Inquilino)
