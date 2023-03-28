from django.db import models
#Modulo de Stock productos
# Create your models here.
#Modelo de Stock
class Stock(models.Model):
    id_stock_producto=models.AutoField(primary_key=True,verbose_name="Id Materia Prima")
    nombre_stock_Producto=models.CharField(max_length=45,verbose_name="")
    cantidad_stock_Producto=models.IntegerField(max_length=10,verbose_name="")
    id_producto=models.ForeignKey("producto.Producto",verbose_name="id Producto")
    id_stock_materia_prima=models.ForeignKey("stock.Materia_Prima",verbose_name="Id Materia Prima")
#Modelo de Materia Prima
class Materia_Prima(models.Model):
    id_materia_prima=models.AutoField(primary_key=True,verbose_name="Id Materia Prima")
    nombre_materia_prima=models.CharField(max_length=45,verbose_name="Nombre de la materia prima")
    cantidad_stock_producto=models.IntegerField(max_length=10,verbose_name="Cantidad en Stock")
    tipo=models.CharField( max_length=50,verbose_name="Tipo")
    color=models.CharField(max_length=50,verbose_name="Color")