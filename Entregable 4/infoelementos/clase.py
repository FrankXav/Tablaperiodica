class Elemento:
    Nombre="Nombre elemento"
    Simbolo="Simbolo"
    Numero_Atomico="Numero Atomico"
    Periodo="Periodo"
    Grupo="Grupo"
    Masa_Atomica="Masa Atomica"
    Densidad="Densidad elemento"
    Categoria="Categoria"
    Informacion="Informacion del elemento"

    def __init__(self,Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion):
        self.Nombre=Nombre
        self.Simbolo=Simbolo
        self.Numero_Atomico=Numero_Atomico
        self.Masa_Atomica=Masa_Atomica
        self.Periodo=Periodo
        self.Grupo=Grupo
        self.Densidad=Densidad
        self.Categoria=Categoria
        self.Informacion=Informacion

    def Imprimir_Info(self):
        print(f'Nombre: {self.Nombre}')
        print(f'Simbolo : {self.Simbolo}')
        print(f'Numero Atomico: {self.Numero_Atomico}')
        print(f'Masa Atomica: {self.Masa_Atomica}')
        print(f'Periodo: {self.Periodo}')
        print(f'Grupo: {self.Grupo}')
        print(f'Densidad: {self.Densidad}')
        print(f'Categoria: {self.Categoria}')
        print(self.Informacion)

    def CorNombre(self):
        self.Nombre = self.Nombre.title()

    def CorMasa_Atomica(self):
        num = ""
        for i in self.Masa_Atomica:
            if i != ",":
                if (i != " ") and (i != 'u'):
                    num = num + i
            else: 
                num = num + "."

        num = float(num)

        self.Masa_Atomica = num


    def CorDensidad(self):
        num = ""
        for i in self.Densidad:
            if i != ",":
                if (i != " ") and (i != 'g') and (i != '/') and (i != 'm') and (i != 'l') and (i != '-'):
                    num = num + i
            else: 
                num = num + "."
    
        try:
            num = float(num)
        except:
            num = ""

        self.Densidad = num

    def CorCategoria(self):
        cat = {'Gases Nobles':1, 'No Metales':2, 'Metales Alcalinos':3, 'Alcalinotérreos':4, 'Metaloides':5, 'Halógenos':6, 'Metales':7, 'Metales de transición':8, 'Lantanidos':9, 'Actinido':10}
        self.Categoria = cat[self.Categoria]

    def CorInformacion(self):
        info = ""

        for i in self.Informacion:
            if i != "\n":
                info = info + i

        if info == '-':
            info = ''

        self.Informacion = info


    def printhtml(self):
        return f'<div class="{self.Nombre}" id="{self.Nombre}" onmouseover="imagen(\'{self.Nombre}\')" onclick="plantilla()"></div>'

    def printcss(self):
        """if (self.Categoria == "Alcalinotérreos"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgba(255, 238, 0, 0.87);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    #print(f'    color: white;')
                                    print('}')
                                elif (self.Categoria == "No Metales"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(255, 102, 0);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    print('}')
                                                
                                elif (self.Categoria == "Gases Nobles"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(7, 59, 0);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    print(f'    color: white;')
                                    print('}')
                                        
                                elif (self.Categoria == "Metales Alcalinos"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(0, 0, 90);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    print(f'    color: white;')
                                    print('}')
                                                
                                elif (self.Categoria == "Metaloides"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(207, 0, 69);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    print(f'    color: white;')
                                    print('}')
                                    
                                elif (self.Categoria == "Halógenos"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(0, 156, 8);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    #print(f'    color: white;')
                                    print('}')
                                        
                                elif (self.Categoria == "Metales"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(98, 0, 122);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    print(f'    color: white;')
                                    print('}')
                                        
                                elif (self.Categoria == "Metales de transición"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(3, 131, 190);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    print(f'    color: white;')
                                    print('}')
                                                
                                elif (self.Categoria == "Lantanidos"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(219, 215, 150);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    #print(f'    color: white;')
                                    print('}')
                                            
                                elif (self.Categoria == "Actinido"):
                                    print(f'.{self.Nombre}', end=" ") 
                                    print('{')
                                    print(f'    grid-area: {self.Nombre.lower()};')
                                    print(f'    background-color: rgb(150, 205, 219);')
                                    print(f'    padding: 0;')
                                    print(f'    margin: 3px;')
                                    #print(f'    color: white;')
                                    print('}')"""

        if (self.Categoria == "Alcalinotérreos"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgba(255, 248, 143, 0.87);')
            print(f'    cursor: pointer;')
            print('}')
        elif (self.Categoria == "No Metales"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(255, 167, 109);')
            print(f'    cursor: pointer;')
            print('}')
                        
        elif (self.Categoria == "Gases Nobles"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(105, 134, 101);')
            print(f'    cursor: pointer;')
            print('}')
                
        elif (self.Categoria == "Metales Alcalinos"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(89, 89, 126);')
            print(f'    cursor: pointer;')
            print('}')
                        
        elif (self.Categoria == "Metaloides"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(231, 137, 168);')
            print(f'    cursor: pointer;')
            print('}')
            
        elif (self.Categoria == "Halógenos"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(129, 192, 132);')
            print(f'    cursor: pointer;')
            print('}')
                
        elif (self.Categoria == "Metales"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(184, 110, 202);')
            print(f'    cursor: pointer;')
            print('}')
                
        elif (self.Categoria == "Metales de transición"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(180, 219, 238);')
            print(f'    cursor: pointer;')
            print(f'    color:black;')
            print('}')
                        
        elif (self.Categoria == "Lantanidos"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(252, 250, 210);')
            print(f'    cursor: pointer;')
            print('}')
                    
        elif (self.Categoria == "Actinido"):
            print(f'.{self.Nombre}:hover', end=" ") 
            print('{')
            print(f'    background-color: rgb(200, 250, 247);')
            print(f'    cursor: pointer;')
            print('}')



