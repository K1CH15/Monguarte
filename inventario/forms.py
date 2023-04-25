
from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Stock

class Materia_PrimaForm(ModelForm):

    class Meta:
        model =Materia_Prima
        fields = "__all__"
        exclude=[""]
class Materia_PrimaUptadeForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        exclude=[""]

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = "__all__"
        exclude=[""]

class StockUptadeForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = "__all__"
        exclude=[""]


