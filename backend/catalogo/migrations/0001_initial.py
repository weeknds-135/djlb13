from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[migrations.CreateModel(name='Categoria',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nombre',models.CharField(max_length=80,unique=True)),('descripcion',models.CharField(blank=True,max_length=240))]),migrations.CreateModel(name='Producto',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nombre',models.CharField(max_length=160)),('descripcion',models.TextField()),('precio',models.DecimalField(decimal_places=2,max_digits=8)),('imagen',models.URLField(blank=True)),('cantidad_disponible',models.PositiveIntegerField(default=0)),('autor',models.CharField(blank=True,max_length=120)),('categoria',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='productos',to='catalogo.categoria'))])]
