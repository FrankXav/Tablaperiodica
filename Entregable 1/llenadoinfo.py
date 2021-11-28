termino="no"
Numero_Atomico=112
Periodo = 7
Grupo = 12
while(termino=="no"):    
    Nombre=input("Nombre: ")
    Simbolo=input("Simbolo: ")
    Numero_Atomico=Numero_Atomico+1
    Masa_Atomica = input("Masa_Atomica: ")
    Grupo=Grupo+1
    Categoria=input("Categoria: ")
    #Categoria="Metales de transición"
    Densidad = input("Densidad: ")
    Informacion=input("Informacion: ")
    print(f"#{Nombre}\nNombre='{Nombre}'\nSimbolo='{Simbolo}'\nNumero_Atomico={Numero_Atomico}\nMasa_Atomica = '{Masa_Atomica} u'\nPeriodo={Periodo}\nGrupo={Grupo}\nCategoria='{Categoria}'\nDensidad = '{Densidad} g/ml'\nInformacion='''{Informacion}'''\n{Nombre}=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)\nListaElementos.append({Nombre})")