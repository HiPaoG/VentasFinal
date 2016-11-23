from django.db import models
from django.contrib import admin
from django.utils import timezone

class Producto(models.Model):
    COMIDA = 'CO'
    ROPA = 'RO'
    ZAPATOS = 'ZA'
    JUEGOS = 'JU'
    MARCAS = (
        (COMIDA, 'Comida'),
        (ROPA, 'Ropa'),
        (ZAPATOS, 'Zapatos'),
        (JUEGOS, 'Juegos'),
    )
    codigo = models.CharField(max_length=7)
    nombre = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='photo/')
    marca = models.CharField(max_length=2, choices=MARCAS, default=COMIDA,)
    precio = models.DecimalField(max_digits=5, decimal_places=2,)
    existencia = models.IntegerField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    dpi = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto, through='Compra')

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now=True)

class CompraInLine(admin.TabularInline):
    model = Compra
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (CompraInLine,)

class UsuarioAdmin (admin.ModelAdmin):
    inlines = (CompraInLine,)
