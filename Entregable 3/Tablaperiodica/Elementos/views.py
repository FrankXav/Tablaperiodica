from rest_framework import filters
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Elementos.models import Elemento 

from .serializers import *

# Create your views here.

class CategoriaList(generics.ListAPIView):
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

class ElementosList(generics.ListAPIView):
    serializer_class = ElementoSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

class ElementoCreate(generics.CreateAPIView):
    serializer_class = ElementoSerializer

    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Elemento creado'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ElementoDetail(generics.RetrieveAPIView):
    serializer_class = ElementoSerializer
    lookup_field = 'Nombre'
    
    def get_queryset(self):
        Nombre = self.kwargs['Nombre']
        return Elemento.objects.filter(Nombre=Nombre)

class ElementoDelete(generics.DestroyAPIView):
    serializer_class = ElementoSerializer
    lookup_field = 'Nombre'
    
    def get_queryset(self):
        Nombre = self.kwargs['Nombre']
        return Elemento.objects.filter(Nombre=Nombre)

    def delete(self, request, Nombre=None):
        Elemento = self.get_queryset()
        if Elemento:
            self.destroy(request, Nombre)
            return Response({'message':'Elemento Eliminado'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ElementoUpdate(generics.UpdateAPIView):
    serializer_class = ElementoSerializer
    lookup_field = 'Nombre'

    def get_queryset(self, Nombre):
        Nombre = self.kwargs['Nombre']
        return Elemento.objects.filter(Nombre=Nombre).first()

    def patch(self, request, Nombre=None):
        elemento = self.get_queryset(Nombre)
        if elemento:
            elemento_serializer = self.serializer_class(elemento)
            return Response(data=elemento_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'No existe producto'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, Nombre=None):
        if self.get_queryset(Nombre):
            Elemento_serializer =self.serializer_class(self.get_queryset(Nombre),data = request.data)
            if Elemento_serializer.is_valid():
                Elemento_serializer.save()
                return Response(Elemento_serializer.data, status=status.HTTP_200_OK)
            return Response(Elemento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ElementoListFilter(generics.ListAPIView):

    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Nombre','Simbolo', 'No_Atomico','Categoria', 'Grupo', 'Periodo', "Masa_Atomica", "Densidad"]




    
