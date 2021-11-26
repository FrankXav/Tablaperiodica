import os
from clase import Elemento
from funciones import Pedir_Elemento, Probar_opcion

Os="Windows"
if(Os=="Windows"):
    Limpiar="cls"
else:
    Limpiar="clear"

os.system(Limpiar)
salir="si"
while(salir=="si"):
    print('''Proyecto tabla periodica
    Que desea realizar:
    1.- Ver elementos que conforman un grupo en especifico
    2.- Ver informacion de algun elemento
    3.- Salir''')
    opcion=input("Ingrese en forma numerica una opcion: ")
    opcion=Probar_opcion(opcion)
    if(opcion==1):
        pass
        os.system(Limpiar)
    elif(opcion==2):
        Elemento = Pedir_Elemento()
        os.system(Limpiar)
        Elemento.Imprimir_Info()
        salir=input("Quiere ver la inforacion de otro elemento?: ")
        os.system(Limpiar)
    elif(opcion==3):
        print("Salir")
        exit()
    else:
        print("Opcion no valida")
    if(salir=="no"):
        print("Salir")