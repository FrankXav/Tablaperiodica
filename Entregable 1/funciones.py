from informacion import Ini_Hidrogeno 

Hidrogeno=Ini_Hidrogeno()

def Pedir_Elemento():
    Elementos = {"hidrogeno":"h", "helio":"he" }
    Elementosreturn = {"hidrogeno":Hidrogeno}
    Elemento=input("Ingrese el nombre o simbolo del elemento que desea saber su informacion: ").lower()
    if (Elemento in Elementos):
        for key in Elementosreturn:
            if(key==Elemento):
                return Elementosreturn[key]
    elif(len(Elemento)<=2):
        for key in Elementos:
            if(Elemento==Elementos[key]):
                Elemento=key
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
    else:
        print("Elemento no encontrado")
        Intento=input("Desea intenar de nuevo? (si o no): ").lower()
        if(Intento=="si"):
            Elemento=Pedir_Elemento()
            return Elemento
        else:
            exit()
