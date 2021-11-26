from clase import Elemento

#Hidrogeno

Nombre="Hidrogeno"
Simbolo="H"
Numero_Atomico=1
Peso_atomico = 2
Periodo=4
Grupo=1
Categoria="Metales"
Densidad = 34
Informacion="Info Hisrogeno"

def Ini_Hidrogeno():
    Hidrogeno=Elemento(Nombre,Simbolo,Numero_Atomico,Peso_atomico,Periodo,Grupo,Densidad,Categoria,Informacion)
    return Hidrogeno
