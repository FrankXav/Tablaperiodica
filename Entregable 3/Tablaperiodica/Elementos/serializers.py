from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Periodo
        fields = '__all__'

class ElementoSerializer(serializers.ModelSerializer):
    """ Grupo = GrupoSerializer()
    Periodo = PeriodoSerializer()
    Categoria = CategoriaSerializer()
    Creado_por = UserSerializer() """

    class Meta:
        model = Elemento
        exclude = ('Creado_por',)

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'Nombre': instance.Nombre,
            'Simbolo': instance.Simbolo,
            'No_Atomico': instance.No_Atomico,
            'Periodo': instance.Periodo.No_Periodo,
            'Grupo': instance.Grupo.No_Grupo,
            'Masa_Atomica': instance.Masa_Atomica,
            'Densidad': instance.Densidad,
            'Categoria': instance.Categoria.Categoria,
            #'Creado_por': instance.Creado_por.Nickname,
            'Informacion': instance.Informacion

        }