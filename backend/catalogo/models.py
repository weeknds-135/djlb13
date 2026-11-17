from django.db import models
class Categoria(models.Model):
 nombre=models.CharField(max_length=80,unique=True)
 descripcion=models.CharField(max_length=240,blank=True)
 def __str__(self): return self.nombre
class Producto(models.Model):
 nombre=models.CharField(max_length=160)
 descripcion=models.TextField()
 precio=models.DecimalField(max_digits=8,decimal_places=2)
 imagen=models.URLField(blank=True)
 cantidad_disponible=models.PositiveIntegerField(default=0)
 categoria=models.ForeignKey(Categoria,related_name='productos',on_delete=models.PROTECT)
 autor=models.CharField(max_length=120,blank=True)
 def __str__(self): return self.nombre
