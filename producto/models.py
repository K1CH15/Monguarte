from django.db import models
#Modelo del módulo Productos
# Create your models here.
class Producto(models.Model):
    #Modelo de producto
    id_producto=models.AutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=45,verbose_name="Nombre del producto")
    precio_unidad_producto=models.FloatField(max_length=10,verbose_name="Precio unitario")
    cantidad_producto=models.IntegerField(max_length=10,verbose_name="Cantidad de productos")
    id_tipo_producto=models.ForeignKey("producto.Tipo_Producto")
    id_tamaño_producto=models.ForeignKey("producto.Tamaño_Producto")
    id_stock_producto=models.ForeignKey("stock.Stock")

#Modelo de Tipo de Producto
class Tipo_Producto(models.Model):
    #llave
    id_tipo_producto=models.AutoField(primary_key=True)
    nombre_tipo_producto=models.CharField(max_length=45,verbose_name="Tipo de Producto")
#Modelo de Tamaño Producto
class Tamaño_Producto(models.Model):
    id_tamaño_producto=models.AutoField(primary_key=True)
    nombre_tamaño_producto=models.CharField(max_length=45,verbose_name="Tamaño")