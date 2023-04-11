from django import forms
from django.forms import ModelForm
from usuario.models import Persona,Contabilidad,Aporte,Ips,Nomina,Trabajador
#fORMULARIOS
#formularios Persona
class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = "__all__"
class PersonaUptadeForm(ModelForm):

    class Meta:
        model = Persona
        fields = "__all__"
        exclude = ["id","tipo_documento","numero_documento","rol","estado"]

class ContabilidadForm(ModelForm):

    class Meta:
        model =Contabilidad
        fields = "__all__"

class ContabilidadUptadeForm(ModelForm):

    class Meta:
        model = Contabilidad
        fields = "__all__"
        exclude=["id","tipo","fecha","estado"]

class AporteForm(ModelForm):

    class Meta:
        model = Aporte
        fields = "__all__"

class AporteUptadeForm(ModelForm):

    class Meta:
        model = Aporte
        fields = "__all__"
        exclude=["id","fecha","estado"]

class IpsForm(ModelForm):

    class Meta:
        model = Ips
        fields = "__all__"

class IpsUptadeForm(ModelForm):

    class Meta:
        model = Ips
        fields = "__all__"
        exclude=["id","estado"]

class NominaForm(ModelForm):

    class Meta:
        model = Nomina
        fields = "__all__"

class NominaUptadeForm(ModelForm):

    class Meta:
        model = Nomina
        fields = "__all__"
        exclude=["id","fecha"]

class TrabajadorForm(ModelForm):

    class Meta:
        model = Trabajador
        fields = "__all__"

class TrabajadorUptadeForm(forms.ModelForm):

    class Meta:
        model = Trabajador
        fields = "__all__"
        



