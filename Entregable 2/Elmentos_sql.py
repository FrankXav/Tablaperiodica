from funciones import ListaElementos
from informacion import LiEle

ListaElementos=LiEle()

'''tamañoinfom=0

for i in ListaElementos:
    if(len(i.Informacion)>tamañoinfom):
        tamañoinfom=len(i.Informacion)

print(tamañoinfom)'''
f=open('scriptinfo.txt','w')


id=1
info=""
info2=[]
infof=''
contador=0
for i in ListaElementos:
    f.write(f'INSERT INTO public.elemento(\n')
    f.write(f'    id, nombre, simbolo, no_atomico, masa_atomica, periodo, grupo, densidad, categoria, informacion)\n')
    info=i.Informacion
    info=''
    for x in info:
        if (x != "\n"):
            infof=infof+x
    f.write(f"    VALUES ({id},'{i.Nombre}','{i.Simbolo}',{i.Numero_Atomico},'{i.Masa_Atomica}',{i.Periodo},{i.Grupo},'{i.Densidad}','{i.Categoria}','{infof}');\n")
    id=id+1