from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Fabricacion
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
        exclude = ['estado']


class FabricacionUptadeForm(ModelForm):

    class Meta:
        model = Fabricacion
        fields = "__all__"

# class StockForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['materia_prima', 'cantidad', 'precio_unitario']
