from django.db import models

# Create your models here.
class Categoria(models.Model):
        nombre = models.CharField(max_length=100)
        pub_date = models.DateTimeField("fecha de registro",auto_now=True)

        def __str__(self):
                return self.nombre

class Tienda(models.Model):
        tipo_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
        nombre = models.CharField(max_length=200)
        cantidad = models.DecimalField("Cantidad por unidad",max_digits=6,decimal_places=2)
        unidad = models.CharField("Unidad de medida",max_length=100)
        precio = models.DecimalField("Precio unitario",max_digits=6,decimal_places=2)
        stock = models.IntegerField(default=0)
        descripcion = models.CharField(max_length=500)
        imagen = models.ImageField(upload_to='productos/',null=True, blank=True)
        pub_date = models.DateTimeField("Fecha de publicación")

        def __str__(self):
                return self.nombre



