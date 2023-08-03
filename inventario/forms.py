from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Unidad_Medida,Fabricacion
class Materia_PrimaForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude=["estado"]
class Materia_PrimaUptadeForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        

class Unidad_MedidaForm(ModelForm):
    class Meta:
        model = Unidad_Medida
        fields = "__all__"
        exclude=["estado"]

class Unidad_MedidaUptadeForm(ModelForm):

    class Meta:
        model = Unidad_Medida
        fields = "__all__"


class FabricacionForm(ModelForm):

    class Meta:
        model = Fabricacion
        fields = "__all__"


class FabricacionUptadeForm(ModelForm):

    class Meta:
        model = Fabricacion
        fields = "__all__"

# class Detalle_ProductoForm(ModelForm):
#
#     class Meta:
#         model = Detalle_Producto
#         fields = "__all__"
#         exclude=["estado"]
#
# class Detalle_ProductoUptadeForm(ModelForm):
#
#     class Meta:
#         model = Detalle_Producto
#         fields = "__all__"
