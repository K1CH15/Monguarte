from django.forms import ModelForm, widgets
from productos.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        exclude=["estado"]
        # fields= ["Id",NombreProducto","PrecioUniario","CantidadProducto"]
        
class ProductoUpdateForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        exclude=["estado"]

# class TamañoForm(ModelForm):
#     class Meta:
#         model = Tamaño
#         fields = "__all__"
#         exclude=["estado",]
#         # fields= ["Id",Nombre"]
#
# class TamañoUpdateForm(ModelForm):
#     class Meta:
#         model = Tamaño
#         fields = "__all__"
#
# class TipoForm(ModelForm):
#     class Meta:
#         model = Tipo
#         fields = "__all__"
#         exclude=["estado",]
#         # fields= ["Id",Nombre"]
#
# class TipoUpdateForm(ModelForm):
#     class Meta:
#         model = Tipo
#         fields = "__all__"
