from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Fabricacion
class Materia_PrimaForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude=["estado","stock"]
class Materia_PrimaUptadeForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude = ["estado", "stock"]
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
