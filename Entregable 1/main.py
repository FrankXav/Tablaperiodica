import os
from clase import Elemento
from funciones import Pedir_Elemento

os.system("cls")
salir="si"
while(salir=="si"):
    print('''Proyecto tabla periodica
    Que desea realizar:
    1.- Ver elementos que conforman un grupo en especifico
    2.- Ver informacion de algun elemento
    3.- Salir''')
    opcion=int(input("Ingrese en forma numerica una opcion: "))
    if(opcion==1):
        pass
        os.system("cls")
    elif(opcion==2):
        Elemento = Pedir_Elemento()
        os.system("cls")
        Elemento.Imprimir_Info()
        salir=input("Quiere ver la inforacion de otro elemento?: ")
        os.system("cls")
    elif(opcion==3):
        print("Salir")
        exit()
    else:
        print("Opcion no valida")
    if(salir=="no"):
        print("Salir")