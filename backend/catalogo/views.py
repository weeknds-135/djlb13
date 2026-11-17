from rest_framework import viewsets
from .models import Categoria,Producto
from .serializers import CategoriaSerializer,ProductoSerializer
class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
 queryset=Categoria.objects.all().order_by('nombre'); serializer_class=CategoriaSerializer
class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
 queryset=Producto.objects.select_related('categoria').all().order_by('nombre'); serializer_class=ProductoSerializer
