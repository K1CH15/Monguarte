from django import forms
from django.forms import ModelForm
from venta.models import Detalle_Venta, Venta

class Detalle_VentaForm(ModelForm):
    class Meta:
        model = Detalle_Venta
        fields = '__all__'
class Detalle_VentaUpdateForm(ModelForm):
    class Meta:
        model = Detalle_Venta
        fields = '__all__'

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
class VentaUpdateForm(ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        #exclude = ["estado"]

