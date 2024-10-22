from rest_framework import viewsets
from .serializer import CrudSerializer
from .models import Crud
 

 # Esta clase crea todas las funcion del CRUD 
class CrudView(viewsets.ModelViewSet):
    serializer_class = CrudSerializer
    queryset = Crud.objects.all()