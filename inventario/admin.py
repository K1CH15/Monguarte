from django.contrib import admin

# Register your models here.
from inventario.models import Materia_Prima
from inventario.models import Fabricacion
from inventario.models import Unidad_Medida

admin.site.register(Materia_Prima)
admin.site.register(Fabricacion)
admin.site.register(Unidad_Medida)