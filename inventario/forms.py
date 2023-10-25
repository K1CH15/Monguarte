from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Fabricacion
from django_select2.forms import Select2Widget

class Materia_PrimaForm(ModelForm):
    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude=["estado","stock","precio_unidad"]

class Materia_PrimaUptadeForm(ModelForm):
    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude = ["estado", "stock","precio_unidad"]

class FabricacionForm(ModelForm):
    # Modifica el campo materia_prima para utilizar el widget Select2
    materia_prima = forms.ModelChoiceField(
        queryset=Materia_Prima.objects.all(),
        widget=Select2Widget,  # Utiliza el widget Select2
    )

    class Meta:
        model = Fabricacion
        fields = "__all__"
        exclude = ['estado']


class FabricacionUptadeForm(ModelForm):
    # Modifica el campo materia_prima para utilizar el widget Select2
    materia_prima = forms.ModelChoiceField(
        queryset=Materia_Prima.objects.all(),
        widget=Select2Widget,  # Utiliza el widget Select2
    )

    class Meta:
        model = Fabricacion
        fields = "__all__"

# class StockForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['materia_prima', 'cantidad', 'precio_unitario']
