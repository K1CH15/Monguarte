from django.forms import ModelForm
from compra.models import Compra,Detalle_Compra
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = "__all__"
        exclude = ["estado"]
        success_message = 'la compra se añadió correctamente'
class CompraUpdateForm(ModelForm):
    class Meta:
        model = Compra
        fields ="__all__"
        exclude=["id","fecha"]
        success_message = 'la compra se actualizó correctamente'

class Detalle_CompraForm(ModelForm):
    class Meta:
        model = Detalle_Compra
        fields = "__all__"
        success_message = 'el detalle de la compra se añadió correctamente'


class Detalle_CompraUpdateForm(ModelForm):

    class Meta:
        model = Detalle_Compra
        fields = "__all__"
        exclude =["id"]
        success_message = 'el detalle de la compra se actualizó correctamente'

