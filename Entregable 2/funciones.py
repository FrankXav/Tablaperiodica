#from clase import Elemento
from informacion import LiEle, Periodo

ListaElementos=LiEle()

def LsitaElementos():
    Elementos={}
    for Elemento in ListaElementos:
        Elementos[Elemento.Nombre.lower()]=Elemento.Simbolo.lower()
        #print(Elementos)
    return Elementos

def LReturn():
    Elementos={}
    for Elemento in ListaElementos:
        Elementos[Elemento.Nombre.lower()]=Elemento
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
            #print(f'{Elemento}=={Elementos[key]}')
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
        if(opcion>=5):
            print("Opcion no valida, prueba de nuevo")
            opcion=input("Ingrese de forma numerica una opcion: ")
            opcion=Probar_opcion(opcion)
    except:
        print("Opcion no valida, prueba de nuevo")
        opcion=input("Ingrese de forma numerica una opcion: ")
        opcion=Probar_opcion(opcion)
    return opcion

def MosEGrupo():
    Grupo=input("Ingrese el grupo para ver los elementos que lo conforman: ")
    GrupValidos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    try:
        Grupo=int(Grupo)
    except:
        print("Opcion no valida")
        LGElementos= MosEGrupo()
    if(Grupo in GrupValidos):
        LGElementos=[]
        for Elemento in ListaElementos:
            if(Elemento.Grupo==Grupo):
                LGElementos.append(Elemento.Nombre)
        #return LGElementos
    else:
        print("Opcion no valida")
        LGElementos= MosEGrupo()
    return LGElementos

def MosEPeriodo():
    Periodo=input("Ingrese el periodo para ver los elementos que lo conforman:  ")
    PValidos=[1,2,3,4,5,6,7]
    try:
        Periodo=int(Periodo)
    except:
        print("Opcion no valida")
        LPElementos= MosEPeriodo()
    if(Periodo in PValidos):
        LPElementos=[]
        for Elemento in ListaElementos:
            if(Elemento.Periodo==Periodo):
                LPElementos.append(Elemento.Nombre)
        #return LGElementos
    else:
        print("Opcion no valida")
        LPElementos= MosEPeriodo()
    return LPElementos

