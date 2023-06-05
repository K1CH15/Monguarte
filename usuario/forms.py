from django import forms
from django.forms import ModelForm
from usuario.models import Persona,Contabilidad,Aporte,Ips,Nomina,Trabajador


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
        exclude = ["id","tipo_documento","numero_documento","rol"]

class ContabilidadForm(ModelForm):

    class Meta:
        model =Contabilidad
        fields = "__all__"
        exclude = ["estado"]

class ContabilidadUptadeForm(ModelForm):

    class Meta:
        model = Contabilidad
        fields = "__all__"
        exclude=["id","tipo","fecha"]

class AporteForm(ModelForm):

    class Meta:
        model = Aporte
        fields = "__all__"
        exclude = ["estado"]

class AporteUptadeForm(ModelForm):

    class Meta:
        model = Aporte
        fields = "__all__"
        exclude=["id","fecha","estado"]

class IpsForm(ModelForm):

    class Meta:
        model = Ips
        fields = "__all__"
        exclude = ["estado"]

class IpsUptadeForm(ModelForm):

    class Meta:
        model = Ips
        fields = "__all__"
        exclude=["id","estado"]

class NominaForm(ModelForm):

    class Meta:
        model = Nomina
        fields = "__all__"
        exclude=["estado"]
class NominaUptadeForm(ModelForm):

    class Meta:
        model = Nomina
        fields = "__all__"
        exclude=["id","fecha","estado"]

class TrabajadorForm(ModelForm):

    class Meta:
        model = Trabajador
        fields = "__all__"
        
class TrabajadorUptadeForm(forms.ModelForm):

    class Meta:
        model = Trabajador
        fields = "__all__"
        



