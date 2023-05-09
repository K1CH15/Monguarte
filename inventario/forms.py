
from django import forms
from django.forms import ModelForm
from inventario.models import Materia_Prima,Stock_Producto,Stock_Materia_Prima,Detalle_Producto
class Materia_PrimaForm(ModelForm):

    class Meta:
        model =Materia_Prima
        fields = "__all__"
        exclude=["estado"]
class Materia_PrimaUptadeForm(ModelForm):

    class Meta:
        model = Materia_Prima
        fields = "__all__"
        

class Stock_ProductoForm(ModelForm):

    class Meta:
        model = Stock_Producto
        fields = "__all__"
        exclude=["estado"]

class Stock_ProductoUptadeForm(ModelForm):

    class Meta:
        model = Stock_Producto
        fields = "__all__"
        

class Stock_Materia_PrimaForm(ModelForm):

    class Meta:
        model = Stock_Materia_Prima
        fields = "__all__"
        exclude=["estado"]

class Stock_Materia_PrimaUptadeForm(ModelForm):

    class Meta:
        model = Stock_Materia_Prima
        fields = "__all__"

class Detalle_ProductoForm(ModelForm):

    class Meta:
        model = Detalle_Producto
        fields = "__all__"
        exclude=["estado"]

class Detalle_ProductoUptadeForm(ModelForm):

    class Meta:
        model = Detalle_Producto
        fields = "__all__"
