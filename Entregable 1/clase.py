class Elemento:
    Nombre="Nombre elemento"
    Simbolo="Simbolo"
    Numero_Atomico="Numero Atomico"
    Periodo="Periodo"
    Grupo="Grupo"
    Peso_atomico="Peso Atomico"
    Densidad="Densidad elemento"
    Categoria="Categoria"
    Informacion="Informacion del elemento"

    def __init__(self,Nombre,Simbolo,Numero_Atomico,Peso_atomico,Periodo,Grupo,Densidad,Categoria,Informacion):
        self.Nombre=Nombre
        self.Simbolo=Simbolo
        self.Numero_Atomico=Numero_Atomico
        self.Peso_atomico=Peso_atomico
        self.Periodo=Periodo
        self.Grupo=Grupo
        self.Densidad=Densidad
        self.Categoria=Categoria
        self.Informacion=Informacion

    def Imprimir_Info(self):
        print(f'Nombre: {self.Nombre}')
        print(f'Simbolo : {self.Simbolo}')
        print(f'Numero Atomico: {self.Numero_Atomico}')
        print(f'Peso Atomico: {self.Peso_atomico}')
        print(f'Periodo: {self.Periodo}')
        print(f'Grupo: {self.Grupo}')
        print(f'Densidad: {self.Densidad}')
        print(f'Categoria: {self.Categoria}')
        print(self.Informacion)



