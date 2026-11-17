from django.core.management.base import BaseCommand
from catalogo.models import Categoria,Producto
class Command(BaseCommand):
 help='Carga categorías y libros de demostración para Lima Lectora.'
 def handle(self,*args,**kwargs):
  data={'Narrativa peruana':[('La ciudad y los perros','Una mirada intensa a la vida en el Colegio Militar Leoncio Prado.',49.90,8,'Mario Vargas Llosa'),('Los gallinazos sin plumas','Relatos urbanos sobre la infancia y la desigualdad en Lima.',35.00,12,'Julio Ramón Ribeyro')],'Poesía':[('Canto villano','Poesía esencial de una de las voces más singulares del Perú.',42.00,6,'Blanca Varela')],'Lecturas para aprender':[('El mundo es ancho y ajeno','Una novela fundamental sobre comunidad, memoria y territorio.',55.50,5,'Ciro Alegría')]}
  for category,products in data.items():
   cat,_=Categoria.objects.get_or_create(nombre=category,defaults={'descripcion':f'Selección de {category.lower()}.'})
   for name,description,price,stock,author in products: Producto.objects.get_or_create(nombre=name,defaults={'descripcion':description,'precio':price,'cantidad_disponible':stock,'categoria':cat,'autor':author})
  self.stdout.write(self.style.SUCCESS('Catálogo de ejemplo cargado.'))
