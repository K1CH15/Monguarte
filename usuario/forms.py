from django import forms
from django.forms import ModelForm
from usuario.models import Persona,Comision


#fORMULARIOS
#formularios Persona
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        exclude=["estado"]

class PersonaUptadeForm(ModelForm):

    class Meta:
        model = Persona
        fields = "__all__"
        exclude = ["id","rol"]

class ComisionForm(ModelForm):

    class Meta:
        model = Comision
        fields = "__all__"


class ComisionUptadeForm(ModelForm):

    class Meta:
        model = Comision
        fields = "__all__"


# class AporteForm(ModelForm):
#
#     class Meta:
#         model = Aporte
#         fields = "__all__"
#         exclude = ["estado"]
#
# class AporteUptadeForm(ModelForm):
#
#     class Meta:
#         model = Aporte
#         fields = "__all__"
#         exclude=["id","fecha","estado"]
#
# class IpsForm(ModelForm):
#
#     class Meta:
#         model = Ips
#         fields = "__all__"
#         exclude = ["estado"]
#
# class IpsUptadeForm(ModelForm):
#
#     class Meta:
#         model = Ips
#         fields = "__all__"
#         exclude=["id","estado"]
#
# class NominaForm(ModelForm):
#
#     class Meta:
#         model = Nomina
#         fields = "__all__"
#         exclude=["estado"]
# class NominaUptadeForm(ModelForm):
#
#     class Meta:
#         model = Nomina
#         fields = "__all__"
#         exclude=["id","fecha","estado"]
#
# class TrabajadorForm(ModelForm):
#
#     class Meta:
#         model = Trabajador
#         fields = "__all__"
#
# class TrabajadorUptadeForm(forms.ModelForm):
#
#     class Meta:
#         model = Trabajador
#         fields = "__all__"
        



