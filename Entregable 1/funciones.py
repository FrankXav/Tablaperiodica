from clase import Elemento
from informacion import InfoHelio, InfoHidrogeno, InfoLitio

#Incializacmos Elementos
Info=InfoHidrogeno()
Hidrogeno = Elemento(Info[0],Info[1],Info[2],Info[3],Info[4],Info[5],Info[6],Info[7],Info[8])

Info=InfoHelio()
Helio = Elemento(Info[0],Info[1],Info[2],Info[3],Info[4],Info[5],Info[6],Info[7],Info[8])

Info=InfoLitio()
Litio = Elemento(Info[0],Info[1],Info[2],Info[3],Info[4],Info[5],Info[6],Info[7],Info[8])

ListaElementos=[Hidrogeno,Helio,Litio]


def LsitaElementos():
    Elementos={}
    for i in ListaElementos:
        Elementos[i.Nombre.lower()]=i.Simbolo.lower()
        #print(Elementos)
    return Elementos

def LReturn():
    Elementos={}
    for i in ListaElementos:
        Elementos[i.Nombre.lower()]=i
        #print(Elementos)
    return Elementos

def Pedir_Elemento():
    Elementos = LsitaElementos()
    #print(Elementos)
    Elementosreturn = LReturn()
    Elemento=input("Ingrese el nombre o simbolo del elemento que desea saber su informacion: ").lower()
    if (Elemento in Elementos):
        for key in Elementosreturn:
            if(key==Elemento):
                return Elementosreturn[key]
    elif(len(Elemento)<=2):
        #print(Elemento)
        for key in Elementos:
            print(f'{Elemento}=={Elementos[key]}')
            if(Elemento==Elementos[key]):
                Elemento=key
        if(len(Elemento)<=2):
            print("Elemento no encontrado")
            Intento=input("Desea intenar de nuevo? (si o no): ").lower()
            if(Intento=="si"):
                Elemento=Pedir_Elemento()
                return Elemento
            else:
                exit()
        else:
            for key in Elementosreturn:
                if(key==Elemento):
                    return Elementosreturn[key]
    else:
        print("Elemento no encontrado")
        Intento=input("Desea intenar de nuevo? (si o no): ").lower()
        if(Intento=="si"):
            Elemento=Pedir_Elemento()
            return Elemento
        else:
            exit()


def Probar_opcion(opcion):
    try:
        opcion=int(opcion)
        if(opcion>=4):
            print("Opcion no valida, prueba de nuevo")
            opcion=input("Ingrese de forma numerica una opcion: ")
            opcion=Probar_opcion(opcion)
    except:
        print("Opcion no valida, prueba de nuevo")
        opcion=input("Ingrese de forma numerica una opcion: ")
        opcion=Probar_opcion(opcion)
    return opcion