from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Fabricacion, Fabricacion_Detalle
class Materia_PrimaForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude=["estado","stock","precio_unitario"]
class Materia_PrimaUptadeForm(ModelForm):

    class Meta:
        
        model = Materia_Prima
        fields = "__all__"
        exclude = ["estado", "stock","precio_unitario"]
class FabricacionForm(ModelForm):
    class Meta:
        model = Fabricacion
        fields = "__all__"
        exclude = ['estado','materia_prima','cantidad_materia','costo_fabricacion']


class FabricacionUptadeForm(ModelForm):
    class Meta:
        model = Fabricacion
        fields = "__all__"
        exclude = ['estado', 'materia_prima', 'cantidad_materia','costo_fabricacion']

class Fabricacion_DetalleForm(ModelForm):

    class Meta:
        model = Fabricacion_Detalle
        fields = "__all__"
        exclude = ['fabricacion','estado']

class Fabricacion_DetalleUptadeForm(ModelForm):
    class Meta:
        model = Fabricacion_Detalle
        fields = "__all__"
        exclude = ['fabricacion', 'estado']
# class StockForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['materia_prima', 'cantidad', 'precio_unitario']
