from clase import Elemento
#from funciones import Hidrogeno

ListaElementos=[]

#Hidrogeno
Nombre="Hidrogeno"
Simbolo="H"
Numero_Atomico= 1
Masa_Atomica = "1.00784 u"
Periodo=1
Grupo=1
Categoria="No Metales"
Densidad = "0,071 g/ml"
Informacion='''Primer elemento de la tabla periódica. En condiciones normales es un gas incoloro, 
inodoro e insípido, compuesto de moléculas diatómicas, H2. El átomo de hidrógeno, símbolo H, 
consta de un núcleo de unidad de carga positiva y un solo electrón. Es uno de los constituyentes 
principales del agua y de toda la materia orgánica, y está distribuido de manera amplia no sólo 
en la Tierra sino en todo el universo.'''
Hidrogeno=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Hidrogeno)

#print(LElementos)
#Helio
Nombre="Helio"
Simbolo="He"
Numero_Atomico= 2
Masa_Atomica = "4.0026 u"
Periodo=1
Grupo=18
Categoria="Gases Nobles"
Densidad = "34 g/ml"
Informacion='''El helio es un gas incoloro, inodoro e insípido. Tiene menor solubilidad en agua que 
cualquier otro gas. Es el elemento menos reactivo y esencialmente no forma compuesto químicos. La 
densidad y la viscosidad del vapor de helio son muy bajas. La conductividad térmica y el contenido 
calórico son excepcionalmente altos. El helio puede licuarse, pero su temperatura de condensación 
es la más baja de cualquier sustancia conocida.'''
Helio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Helio)

#Litio
Nombre="Litio"
Simbolo="Li"
Numero_Atomico=3
Masa_Atomica = "6.941 u"
Periodo=2
Grupo=1
Categoria="Metales alcalinos"
Densidad = "0.53 g/ml"
Informacion='''El litio encabeza la familia de los metales alcalinos en la tabla periódica. En 
la naturaleza se encuentra como una mezcla de los isótopos Li6 y Li7. Es el metal sólido más 
ligero, es blando, de bajo punto de fusión y reactivo. Muchas propiedades físicas y químicas 
son tan o más parecidas a las de los metales alcalinotérreos que a las de su grupo.'''
Litio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Litio)

#Berilio
Nombre="Berilio"
Simbolo="Be"
Numero_Atomico=4
Masa_Atomica = "9.0122 u"
Periodo=2
Grupo=2
Categoria="alcalinotérreos"
Densidad = "1.85 g/ml"
Informacion='''El berilio, metal raro, es uno de los metales estructurales más ligeros, 
su densidad es cerca de la tercera parte de la del aluminio. El principal uso del berilio 
metálico se encuentra en la manufactura de aleaciones berilio-cobre y en el desarrollo de 
materiales moderadores y reflejantes para reactores nucleares.'''
Berilio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Berilio)

#Boro
Nombre="Boro"
Simbolo="B"
Numero_Atomico=5
Masa_Atomica = "10.811 u"
Periodo=2
Grupo=13
Categoria="Metaloides"
Densidad = "2.34 g/ml"
Informacion='''Tiene tres elementos de valencia y se comporta como no metal. 
Se clasifica como metaloide y es el único elemento no metálico con menos de cuatro 
electrones en la capa externa. El elemento libre se prepara en forma cristalina o 
amorfa. La forma cristalina es un sólido quebradizo, muy duro.'''
Boro=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Boro)

#Carbono
Nombre="Carbono"
Simbolo="C"
Numero_Atomico=6
Masa_Atomica = "12.01115 u"
Periodo=2
Grupo=14
Categoria="No Metales"
Densidad = "2.26 g/ml"
Informacion=''' El carbono elemental existe en dos formas alotrópicas 
cristalinas bien definidas: diamante y grafito. Otras formas con poca 
cristalinidad son carbón vegetal, coque y negro de humo. El carbono 
químicamente puro se prepara por descomposición térmica del azúcar (sacarosa) 
en ausencia de aire.'''
Carbono=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Carbono)

#Nitrogeno
Nombre="Nitrogeno"
Simbolo="N"
Numero_Atomico=7
Masa_Atomica = "14.0067 u"
Periodo=2
Grupo=15
Categoria="No Metales"
Densidad = "0.81 g/ml"
Informacion='''El nitrógeno molecular es el principal constituyente de la atmósfera 
( 78% por volumen de aire seco). Esta concentración es resultado del balance entre la 
fijación del nitrógeno atmosférico por acción bacteriana, eléctrica (relámpagos) y 
química (industrial) y su liberación a través de la descomposición de materias orgánicas 
por bacterias o por combustión.'''
Nitrogeno=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Nitrogeno)

#Oxigeno
Nombre="Oxigeno"
Simbolo="O"
Numero_Atomico=8
Masa_Atomica = "15.9994 u"
Periodo=2
Grupo=16
Categoria="No Metales"
Densidad = "1.429 g/ml"
Informacion='''Es de gran interés por ser el elemento esencial en los procesos de 
respiración de la mayor parte de las células vivas y en los procesos de combustión. 
Es el elemento más abundante en la corteza terrestre. Cerca de una quinta parte (en volumen) 
del aire es oxígeno.'''
Oxigeno=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Oxigeno)

#Fluor
Nombre="Fluor"
Simbolo="F"
Numero_Atomico=9
Masa_Atomica = "18.9984 u"
Periodo=2
Grupo=17
Categoria="Halogenos"
Densidad = "1.11 g/ml"
Informacion='''El flúor elemental es un gas de color amarillo pálido a temperaturas normales. El olor del
elemento es algo que está todavía en duda. La reactividad del elemento es tan grande que reacciona 
con facilidad, a temperatura ambiente, con muchas otras sustancias elementales, entre ellas el azufre, 
el yodo, el fósforo, el bromo y la mayor parte de los metales'''
Fluor=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Fluor)

#Neon
Nombre="Neon"
Simbolo="Ne"
Numero_Atomico=10
Masa_Atomica = "20.179 u"
Periodo=2
Grupo=18
Categoria="Gases Nobles"
Densidad = "1.20 g/ml"
Informacion='''El neón es miembro de la familia de los gases nobles. La única fuente comercial 
del neón es la atmósfera terrestre, aunque se encuentran pequeñas cantidades de neón en el gas
natural, en los minerales y en los meteoritos.
Se usan cantidades considerables de neón en la investigación física de alta energía. '''
Neon=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Neon)

#Sodio
Nombre="Sodio"
Simbolo="Na"
Numero_Atomico=11
Masa_Atomica = "22.9898 u"
Periodo=3
Grupo=1
Categoria="Metales Alcalinos"
Densidad = "0.97 g/ml"
Informacion='''El sodio ocupa el sexto lugar por su abundancia entre todos los elementos de 
la corteza terrestre, que contiene el 2.83 porciento de sodio en sus formas combinadas. El sodio es, 
después del cloro, el segundo elemento más abundante en solución en el agua de mar. '''
Sodio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Sodio)


#Magnesio
Nombre="Magnesio"
Simbolo="Mg"
Numero_Atomico=12
Masa_Atomica = "24.305 u"
Periodo=3
Grupo=2
Categoria="Alcalinotérreos"
Densidad = "1.74 g/ml"
Informacion='''El magnesio es blanco plateado y muy ligero. Los iones magnesio disueltos en el 
agua forman depósitos en tuberías y calderas cuando el agua es dura, es decir, cuando contiene 
demasiado magnesio o calcio. Esto se puede evitar con los ablandadores de agua. Es muy abundante en 
la naturaleza, y se halla en cantidades importanes en muchos minerales rocosos, como la dolomita, 
magnesita, olivina y serpentina.'''
Magnesio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Magnesio)

#Aluminio
Nombre="Aluminio"
Simbolo="Al"
Numero_Atomico=13
Masa_Atomica = "24.305 u"
Periodo=3
Grupo=13
Categoria="Metales"
Densidad = "1.74 g/ml"
Informacion='''El Aluminio es blanco plateado y muy ligero. Los iones Aluminio disueltos en el 
agua forman depósitos en tuberías y calderas cuando el agua es dura, es decir, cuando contiene 
demasiado Aluminio o calcio. Esto se puede evitar con los ablandadores de agua. Es muy abundante en 
la naturaleza, y se halla en cantidades importanes en muchos minerales rocosos, como la dolomita, 
magnesita, olivina y serpentina.'''
Aluminio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Aluminio)

#Silicio
Nombre="Silicio"
Simbolo="Si"
Numero_Atomico=14
Masa_Atomica = "28.086 u"
Periodo=3
Grupo=14
Categoria="Metaloides"
Densidad = "2.33 g/ml"
Informacion='''Es un metaloide con marcado lustre metálico y sumamente quebradizo. Por lo regular, 
es tetravalente en sus compuestos, aunque algunas veces es divalente, y es netamente electropositivo 
en su comportamiento químico. Además, se conocen compuestos de silicio pentacoordinados y hexacoordinados.'''
Silicio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Silicio)

#Fosforo
Nombre="Fosforo"
Simbolo="P"
Numero_Atomico=15
Masa_Atomica = "30.9738 u"
Periodo=3
Grupo=15
Categoria="No Metales"
Densidad = "1.82 g/ml"
Informacion='''El fósforo forma la base de gran número de compuestos, de los cuales los más importantes 
son los fosfatos. En todas las formas de vida, los fosfatos desempeñan un papel esencial en los 
procesos de transferencia de energía, como el metabolismo, la fotosíntesis, la función nerviosa y la 
acción muscular.'''
Fosforo=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Fosforo)

#Azufre
Nombre="Azufre"
Simbolo="S"
Numero_Atomico=16
Masa_Atomica = "32,064 u"
Periodo=3
Grupo=16
Categoria="No Metales"
Densidad = "2,07 g/ml"
Informacion='''Los alótropos del azufre (diferentes formas cristalinas) han sido estudiados ampliamente, 
pero hasta ahora las diversas modificaciones en las cuales existen para cada estado (gas, líquido y sólido) 
del azufre elemental no se han dilucidado por completo.'''
Azufre=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Azufre)

#Cloro
Nombre="Cloro"
Simbolo="Cl"
Numero_Atomico=17
Masa_Atomica = "35,453 u"
Periodo=3
Grupo=17
Categoria="Halogenos"
Densidad = "1,56 g/ml"
Informacion='''El cloro existe como un gas amarillo-verdoso a temperaturas y presiones ordinarias. Es el 
segundo en reactividad entre los halógenos, sólo después del flúor, y de aquí que se encuentre libre en 
la naturaleza sólo a las temperaturas elevadas de los gases volcánicos.'''
Cloro=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cloro)

#Argon
Nombre="Argon"
Simbolo="Ar"
Numero_Atomico=18
Masa_Atomica = "39,948 u"
Periodo=3
Grupo=18
Categoria="Gases Nobles"
Densidad = "1,40 g/ml"
Informacion='''El argón es incoloro, inodoro e insípido. En condiciones normales es un gas pero puede 
licuarse y solidificarse con facilidad. El argón no forma compuestos químicos en el sentido normal de 
la palabra, aunque forma algunos compuestos clatratos débilmente enlazados con agua, hidroquinona y fenol. 
Las moléculas de argón gaseoso son monoatómicas.'''
Argon=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Argon)

#Potasio
Nombre="Potasio"
Simbolo="K"
Numero_Atomico=19
Masa_Atomica = "39,098 u"
Periodo=4
Grupo=1
Categoria="Metales Alcalinos"
Densidad = "0,97 g/ml"
Informacion='''Este metal reactivo es ligero y blando. Se parece mucho al sodio en su comportamiento en forma metálica.
El cloruro de potasio se utiliza principalmente en mezclas fertilizantes. Sirve también como material de partida para 
la manufactura de otros compuestos de potasio (potacio).  El hidróxido de potasio se emplea en la manufactura de 
jabones líquidos y el carbonato de potasio para jabones blandos.'''
Potasio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Potasio)

#Calcio
Nombre="Calcio"
Simbolo="Ca"
Numero_Atomico=20
Masa_Atomica = "40,08 u"
Periodo=4
Grupo=2
Categoria="Alcalinotérreos"
Densidad = "1,55 g/ml"
Informacion='''Los compuestos de calcio constituyen 3.64 porciento de la corteza terrestre. El metal es trimorfo, 
más duro que el sodio, pero más blando que el aluminio. Al igual que el berilio y el aluminio, pero a diferencia de 
los metales alcalinos, no causa quemaduras sobre la piel. Es menos reactivo químicamente que los metales alcalinos y 
que los otros metales alcalinotérreos.'''
Calcio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Calcio)

#Escandio
Nombre="Escandio"
Simbolo="Sc"
Numero_Atomico=21
Masa_Atomica = "44,956 u"
Periodo=4
Grupo=3
Categoria="Metales de transición"
Densidad = "3,0 g/ml"
Informacion='''El óxido y otros compuestos del escandio se emplean como catalizadores en la conversión de ácido 
acético en acetona, en la manufactura de propanol y en la conversión de ácidos dicarboxílicos en cetonas y compuestos 
cíclicos. El tratamiento con solución de sulfato de escandio es un medio económico para mejorar la germinación de 
semillas de muchas especies vegetales.'''
Escandio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Escandio)

#Titanio
Nombre="Titanio"
Simbolo="Ti"
Numero_Atomico=22
Masa_Atomica = "47,90 u"
Periodo=4
Grupo=4
Categoria="Metales de transición"
Densidad = "4,51 g/ml"
Informacion='''Mientras que su comportamiento químico muestra muchas semejanzas con el del silicio y el zirconio, 
como un elemento del primer grupo de transición, la química de la solución acuosa, especialmente de los estados 
de oxidación más bajos, tiene algunas semejanzas con la del cromo y el vanadio.'''
Titanio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Titanio)

#Vanadio
Nombre="Vanadio"
Simbolo="V"
Numero_Atomico=23
Masa_Atomica = "50,942 u"
Periodo=4
Grupo=5
Categoria="Metales de transición"
Densidad = "4,51 g/ml"
Informacion='''Es un metal que se utilizó inicialmente en aleaciones con hierro y acero. Varios de los compuestos 
de vanadio se emplean en la industria química, sobre todo en la fabricación de catalizadores de oxidación, y en 
la industria cerámica como agentes colorantes.'''
Vanadio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Vanadio)

#Cromo
Nombre="Cromo"
Simbolo="Cr"
Numero_Atomico=24
Masa_Atomica = "51,996 u"
Periodo=4
Grupo=6
Categoria="Metales de transición"
Densidad = "7,19 g/ml"
Informacion='''Es un metal que es de color blanco plateado, duro y quebradizo. Sin embargo, es relativamente suave 
y dúctil cuando no está tensionado o cuando está muy puro. Sus principales usos son la producción de aleaciones 
anticorrosivas de gran dureza y resistentes al calor y como recubrimiento para galvanizados.'''
Cromo=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cromo)

#Manganeso
Nombre="Manganeso"
Simbolo="Mn"
Numero_Atomico=25
Masa_Atomica = "54,938 u"
Periodo=4
Grupo=7
Categoria="Metales de transición"
Densidad = "7,43 g/ml"
Informacion='''Es uno de los metales de transición del primer periodo largo de la tabla periódica; se encuentra entre 
el cromo y el hierro. Tiene propiedades en común con ambos metales. Aunque poco conocido o usado en su forma pura, reviste 
gran importancia práctica en la fabricación de acero. El manganeso se oxida con facilidad en el aire para formar una capa 
castaña de óxido. También lo hace a temperaturas elevadas.'''
Manganeso=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Manganeso)

#Hierro
Nombre="Hierro"
Simbolo="Fe"
Numero_Atomico=26
Masa_Atomica = "55,847 u"
Periodo=4
Grupo=8
Categoria="Metales de transición"
Densidad = "7,86 g/ml"
Informacion='''El uso más extenso del hierro (fierro) es para la obtención de aceros estructurales; también se producen 
grandes cantidades de hierro fundido y de hierro forjado. Entre otros usos del hierro y de sus compuestos se tienen la 
fabricación de imanes, tintes (tintas, papel para heliográficas, pigmentos pulidores) y abrasivos (colcótar).'''
Hierro=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Hierro)

#Cobalto
Nombre="Cobalto"
Simbolo="Co"
Numero_Atomico=27
Masa_Atomica = "58,93 u"
Periodo=4
Grupo=9
Categoria="Metales de transición"
Densidad = "8,9 g/ml"
Informacion='''El cobalto se parece al hierro y al níquel, tanto en estado libre como combinado. Se encuentra distribuido 
con amplitud en la naturaleza y forma, aproximadamente, el 0.001 porciento del total de las rocas ígneas de la corteza 
terrestre, en comparación con el 0.02 porciento del níquel. Se halla en meteoritos, estrellas, en el mar, en aguas dulces, 
suelos, plantas, animales y en los nódulos de manganeso encontrados en el fondo del océano.'''
Cobalto=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cobalto)

#Niquel
Nombre="Niquel"
Simbolo="Ni"
Numero_Atomico=28
Masa_Atomica = "58,71 u"
Periodo=4
Grupo=10
Categoria="Metales de transición"
Densidad = "8,9 g/ml"
Informacion='''Es un metal duro, blanco plateado, dúctil y maleable. La mayor parte del níquel comercial se emplea en el 
acero inoxidable y otras aleaciones resistentes a la corrosión. También es importante en monedas como sustituto de la plata. 
El níquel finamente dividido se emplea como catalizador de hidrogenación.'''
Niquel=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Niquel)

#Cobre
Nombre="Cobre"
Simbolo="Cu"
Numero_Atomico=29
Masa_Atomica = "63,54 u"
Periodo=4
Grupo=11
Categoria="Metales de transición"
Densidad = "8,96 g/ml"
Informacion='''Es uno de los metales de transición e importante metal no ferroso. Su utilidad se debe a la combinación de sus 
propiedades químicas, físicas y mecánicas, así como a sus propiedades eléctricas y su abundancia. El cobre fue uno de los 
primeros metales usados por los humanos. La mayor parte del cobre del mundo se obtiene de los sulfuros minerales como la 
calcocita, covelita, calcopirita, bornita y enargita. Los minerales oxidados son la cuprita, tenorita, malaquita, azurita, 
crisocola y brocantita. '''
Cobre=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cobre)

#Zinc
Nombre="Zinc"
Simbolo="Zn"
Numero_Atomico=30
Masa_Atomica = "65,37 u"
Periodo=4
Grupo=12
Categoria="Metales de transición"
Densidad = "7,14 g/ml"
Informacion='''Es un metal maleable, dúctil y de color gris. Los usos más importantes del zinc los constituyen las aleaciones 
y el recubrimiento protector de otros metales. El hierro o el acero recubiertos con zinc se denominan galvanizados, y esto 
puede hacerse por inmersión del artículo en zinc fundido (proceso de hot-dip), depositando zinc electrolíticamente sobre el 
artículo como un baño chapeado (electrogalvanizado), exponiendo el artículo a zinc en polvo cerca de su punto de fusión 
(sherardizing) o rociándolo con zinc fundido (metalizado).'''
Zinc=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Zinc)

#Galio
Nombre="Galio"
Simbolo="Ga"
Numero_Atomico=31
Masa_Atomica = "69,72 u"
Periodo=4
Grupo=13
Categoria="Metal"
Densidad = "5,91 g/ml"
Informacion='''Tiene un gran intervalo de temperatura en el estado líquido, y se ha recomendado su uso en termómetros de 
alta temperatura y manómetros. En aleación con plata y estañó, el galio suple en forma adecuada la amalgama en curaciones 
dentales; también sirve para soldar materiales no metálicos, incluyendo gemas o amtales. El arseniuro de galio puede 
utilizarse en sistemas para transformar movimiento mecánico en impulsos eléctricos. Los artículos sintéticos superconductores 
pueden prepararse por la fabricación de matrices porosas de vanadio o tántalo impregnados con hidruro de galio.'''
Galio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Galio)

#Germanio
Nombre='Germanio'
Simbolo='Ge'
Numero_Atomico=32
Masa_Atomica = '72,59 u'
Periodo=4
Grupo=14
Categoria='Metaloides'
Densidad = '5,32 g/ml'
Informacion=''' El germanio se encuentra muy distribuido en la corteza terrestre con una abundancia de 6.7 partes por millon (ppm). 
El germanio se halla como sulfuro o está asociado a los sulfuros minerales de otros elementos, en particular con los del cobre, zinc, 
plomo, estaño y antimonio. El germanio tiene una apariencia metálica, pero exhibe las propiedades físicas y químicas de un metal sólo 
en condiciones especiales, dado que está localizado en la tabla periódica en donde ocurre la transición de metales a no metales.'''
Germanio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Germanio)

#Arsenico
Nombre='Arsenico'
Simbolo='As'
Numero_Atomico=33
Masa_Atomica = '74,922 u'
Periodo=4
Grupo=15
Categoria='Metaloides'
Densidad = '5,72 g/ml'
Informacion='''Existen tres alótropos o modificaciones polimórficas del arsénico. La forma a cúbica de color amarillo se obtiene por 
condensación del vapor a muy bajas temperaturas. La b polimórfica negra, que es isoestructural con el fósforo negro. Ambas revierten 
a la forma más estable, la l , gris o metálica, del arsénico romboédrico, al calentarlas o por exposición a la luz. La forma metálica 
es un conductor térmico y eléctrico moderado, quebradizo, fácil de romper y de baja ductibilidad.'''
Arsenico=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Arsenico)

#Selenio
Nombre='Selenio'
Simbolo='Se'
Numero_Atomico=34
Masa_Atomica = '78,96 u'
Periodo=4
Grupo=16
Categoria='No metales'
Densidad = '4,79 g/ml'
Informacion='''Los empleos más importantes del selenio son el proceso de fotocopiado xerográfico, la decoloración 
de vidrios teñidos por compuestos de hierro, y también se usa como pigmento en plásticos, pinturas, barnices, 
vidrio y cerámica y tintas. Su utilización en rectificadores ha disminuido por el mayor empleo del silicio y 
el germanio en esta aplicación.'''
Selenio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Selenio)

#Bromo
Nombre='Bromo'
Simbolo='Br'
Numero_Atomico=35
Masa_Atomica = '79,909 u'
Periodo=4
Grupo=17
Categoria='Halogenos'
Densidad = '3,12 g/ml'
Informacion='''Elemento químico, Br, número atómico 35 y peso atómico 79.909, por lo común existe como Br2; 
líquido de olor intenso e irritante, rojo oscuro y de bajo punto de ebullición, pero de alta densidad. Es el 
único elemento no metálico líquido a temperatura y presión normales. Es muy reactivo químicamente; elemento 
del grupo de los halógenos, sus propiedades son intermedias entre las del cloro y las del yodo.'''  
Bromo=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Bromo)

#Kriptón
Nombre='Kriptón'
Simbolo='Kr'
Numero_Atomico=36
Masa_Atomica = '83,80 u'
Periodo=4
Grupo=18
Categoria='Gases Nobles'
Densidad = '2,6 g/ml'
Informacion='''Elemento químico gaseoso, símbolo Kr, número atómico 36 y peso atómico 83.80. El kriptón es 
uno de los gases nobles. Es un gas incoloro, inodoro e insípido. Su principal aplicación es el llenado de 
lámparas eléctricas y aparatos electrónicos de varios tipos. Se utilizan ampliamente mezclas de kriptón-argón 
para llenar lámparas fluorescentes. La única fuente comercial de kriptón estable es el aire, aunque se 
encuentran trazas en minerales y meteoritos.'''
Kriptón=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Kriptón)

#Rubidio
Nombre='Rubidio'
Simbolo='Rb'
Numero_Atomico=37
Masa_Atomica = '85,47 u'
Periodo=5
Grupo=1
Categoria='Metales alcalinos'
Densidad = '1,53 g/ml'
Informacion=''' El rubidio es un metal alcalino, reactivo, ligero y de bajo punto de fusión. La mayor parte de 
los usos de rubidio metálico y de sus compuestos son los mismos que los del cesio y sus compuestos. El metal se 
utiliza en la manufactura de tubos de electrones, y las sales en la producción de vidrio y cerámica.'''
Rubidio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Rubidio)

#Estroncio
Nombre='Estroncio'
Simbolo='Sr'
Numero_Atomico=38
Masa_Atomica = '87,62 u'
Periodo=5
Grupo=2
Categoria='Alcalinotérreos'
Densidad = '2,6 g/ml'
Informacion='''El estroncio es el menos abundante de los metales alcalinotérreos. La corteza de la Tierra contiene 
el 0.042 porciento de estroncio, y este elemento es tan abundante como el cloro y el azufre. Los principales minerales 
son la celestita, SrSO4, y la estroncianita, SrCO3. El nitrato de estrocio se emplea en pirotecnia, señalamiento de 
vías férreas y en fórmulas de balas trazadoras. El hidróxido de estroncio forma con cierto número de ácidos orgánicos 
jabones y grasas de estructura estable.'''
Estroncio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Estroncio)

#Itrio
Nombre='Itrio'
Simbolo='Y'
Numero_Atomico=39
Masa_Atomica = '88,906 u'
Periodo=5
Grupo=3
Categoria='Metales de transición'
Densidad = '4,47 g/ml'
Informacion='''El itrio metálico absorbe hidrógeno, y cuando en aleaciones llega a una composición de YH2, se parece mucho 
a los metales. De hecho, en ciertos niveles de composición la aleación es mejor conductora de la electricidad que el metal puro. 
El itrio forma la matriz de los fósforos de itrio y europio activados, que emiten una luz brillante y roja clara cuando 
son excitados por electrones'''
Itrio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Itrio)

#Circonio
Nombre='Zirconio'
Simbolo='Zr'
Numero_Atomico=40
Masa_Atomica = '91,22 u'
Periodo=5
Grupo=4
Categoria='Metales de transición'
Densidad = '6,49 g/ml'
Informacion='''El zirconio es uno de los elementos más abundantes y está ampliamente distribuido en la corteza terrestre. 
Es muy reactivo químicamente y sólo se halla combinado. En la mayor parte de las reacciones se enlaza con oxígeno en preferencia 
sobre otros elementos, encontrándose en la corteza terrestre sólo como el óxido ZrO2, baddeleyita, o como parte de los 
complejos de óxido, como el zircón, la elpidita y la eudialita.'''
Circonio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Circonio)

#Niobio
Nombre='Niobio'
Simbolo='Nb'
Numero_Atomico=41
Masa_Atomica = '92,906 u'
Periodo=5
Grupo=5
Categoria='Metales de transición'
Densidad = '8,4 g/ml'
Informacion='''Símbolo Nb, número atómico 41 y peso atómico 92.906. En Estados Unidos este elemento se llamó originalmente columbio. 
La industria metalúrgica y los metalurgistas aún utilizan este nombre antiguo. La mayor parte del niobio se usa en aceros inoxidables 
especiales, en aleaciones de alta temperatura y en aleaciones superconductoras como Nb3Sn. El niobio también se utiliza en pilas nucleares.'''
Niobio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Niobio)

#Molibdeno
Nombre='Molibdeno'
Simbolo='Mo'
Numero_Atomico=42
Masa_Atomica = '95,94 u'
Periodo=5
Grupo=6
Categoria='Metales de transición'
Densidad = '10.2 g/ml'
Informacion='''El molibdeno se encuentra en muchas partes del mundo, pero pocos depósitos son lo suficientemente ricos para garantizar 
la recuperación de los costos. La mayor parte del molibdeno proviene de minas donde su recuperación es el objetivo primario de la operación. 
El restante se obtiene como un subproducto de ciertas operaciones del beneficio del cobre.'''
Molibdeno=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Molibdeno)

#Tecnecio
Nombre='Tecnecio'
Simbolo='Tc'
Numero_Atomico=43
Masa_Atomica = '97 u'
Periodo=5
Grupo=7
Categoria='Metales de transición'
Densidad = '11,5 g/ml'
Informacion=''' Fue el primer elemento obtenido de manera artificial en un clclotrón. También se obtiene como el principal constituyente de 
los productos de fisión en un reactor nuclear o, en forma alterna, por la acción de neutrones sobre el 98Mo. El isótopo 99Tc es el más útil en 
la investigación química por su larga vida media: 2 x 105 años. La química del tecnecio se parece mucho a la del renio, y se han preparado
algunos compuestos en muchos casos.'''
Tecnecio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Tecnecio)

#Rutenio
Nombre='Rutenio'
Simbolo='Ru'
Numero_Atomico=44
Masa_Atomica = '101,07 u'
Periodo=5
Grupo=8
Categoria='Metales de transición'
Densidad = '12,2 g/ml'
Informacion='''El rutenio es un metal duro, blanco, manejable sólo a altas temperaturas y con dificultad. Es un excelente catalizador y se 
utiliza en reacciones que incluyen hidrogenación, isomerización, oxidación y reformación. Los usos del rutenio metálico puro son mínimos. 
Es un endurecedor eficaz para el platino y el paladio.'''      
Rutenio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Rutenio)

#Rodio
Nombre='Rodio'
Simbolo='Rh'
Numero_Atomico=45
Masa_Atomica = '102,905 u'
Periodo=5
Grupo=9
Categoria='Metales de transición'
Densidad = '12,4 g/ml'
Informacion='''El rodio es un metal blanco, duro, considerablemente menos dúctil que el platino o el paladio, pero mucho más dúctil 
que cualquier otro metal de este grupo. Se usa principalmente como un elemento de aleación para el platino. Es un excelente catalizador 
para la hidrogenación y es activo en la reformación catalítica de hidrocarburos.'''
Rodio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Rodio)

#Paladio
Nombre='Paladio'
Simbolo='Pd'
Numero_Atomico=46
Masa_Atomica = '106,4 u'
Periodo=5
Grupo=10
Categoria='Metales de transición'
Densidad = '12,0 g/ml'
Informacion='''Es un metal blanco y muy dúctil semejante al platino, al que sigue en abundancia e importancia. El paladio soportado 
sobre carbono o alúmina se emplea como catalizador en ciertos procesos químicos en que intervienen reacciones de hidrogenación en 
fase líquida y gaseosa.'''
Paladio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Paladio)

#Plata
Nombre='Plata'
Simbolo='Ag'
Numero_Atomico=47
Masa_Atomica = '107.9 u'
Periodo=5
Grupo=11
Categoria='Metal de transicion'
Densidad = '10,5 g/ml'
Informacion='''Es un metal lustroso de color blanco-grisáceo. Desde el punto de vista químico, es uno de los 
metales pesados y nobles; desde el punto de vista comercial, es un metal precioso. Hay 25 isótopos de la plata. 
Sus masas atómicas fluctúan entre 102 y 117. En la mayor parte de sus aplicaciones, la plata se alea con uno o 
más metales. La plata, que posee las más altas conductividades térmica y eléctrica de todos los metales.'''
Plata=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Plata)

#Cadmio
Nombre='Cadmio'
Simbolo='Cd'
Numero_Atomico=48
Masa_Atomica = '112.4 u'
Periodo=5
Grupo=12
Categoria='Metales de transición'
Densidad = '8,65 g/ml'
Informacion='''Tiene relación estrecha con el zinc, con el que se encuentra asociado en la naturaleza. 
Es un metal dúctil, de color blanco argentino con un ligero matiz azulado. Es más blando y maleable 
que el zinc, pero poco más duro que el estaño.'''
Cadmio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cadmio)

#Indio
Nombre='Indio'
Simbolo='In'
Numero_Atomico=49
Masa_Atomica = '118.7 u'
Periodo=5
Grupo=13
Categoria='Metales'
Densidad = '7,31 g/ml'
Informacion='''Se encuentra aproximadamente en un 0.000001 porciento en la corteza terrestre y normalmente 
en concentraciones de 0.1 porciento o menores. Se halla distribuido ampliamente en muchas minas y minerales 
y se recobra en gran parte de los conductos de polvo y residuos de las operaciones de procesamiento de zinc.'''
Indio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Indio)

#Estaño
Nombre='Estaño'
Simbolo='Sn'
Numero_Atomico=50
Masa_Atomica = '118.7 u'
Periodo=5
Grupo=14
Categoria='Metales'
Densidad = '7.3 g/ml'
Informacion='''Se funde a baja temperatura; tiene gran fluidez cuando se funde y posee un punto de ebullición 
alto. es suave, flexible y resistente a la corrosión en muchos medios. Una aplicación importante es el 
recubrimiento de envases de acero para conservar alimentos y bebidas. Otros empleos importantes son: aleaciones 
para soldar, bronces, pletres y aleaciones industriales diversas. Los productos químicos de estaño, tanto inorgánicos 
como orgánicos, se utilizan mucho en las industrias de galvanoplastia, cerámica y plásticos, y en la agricultura.'''
Estaño=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Estaño)

#Antimonio
Nombre='Antimonio'
Simbolo='Sb'
Numero_Atomico=51
Masa_Atomica = '121.8 u'
Periodo=5
Grupo=15
Categoria='Metaloides'
Densidad = '6,62 g/ml'
Informacion='''El antimonio no es un elemento abundante en la naturaleza; raras veces se encuentra en forma natural, 
a menudo como una mezcla isomorfa con arsénico: la allemonita. Su símbolo Sb se deriva de la palabra latina stibium. 
El antimonio se presenta en dos formas: amarilla y gris. La forma amarilla es metaestable, y se compone de moléculas 
Sb4, se le encuentra en el vapor de antimonio y es la unidad estructural del antimonio amarillo; la forma gris es metálica, 
la cual cristaliza en capas formando una estructura romboédrica.'''
Antimonio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Antimonio)

#Teluro
Nombre='Teluro'
Simbolo='Te'
Numero_Atomico=52
Masa_Atomica = '127.6 u'
Periodo=5
Grupo=16
Categoria='Metaloides'
Densidad = '6,24 g/ml'
Informacion='''Se encuentra como elemento libre, asociado algunas veces con selenio, y también existe como telururo de 
silvanita (teluro gráfico), nagiagita (telurio negro), hessita, tetradimita, altaita, coloradoita y otros telururos de plata 
y oro, así como el óxido, telurio ocre.'''
Teluro=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Teluro)

#Yodo
Nombre='Yodo'
Simbolo='I'
Numero_Atomico=53
Masa_Atomica = '126.9 u'
Periodo=5
Grupo=17
Categoria='Halogenos'
Densidad = '4,94 g/ml'
Informacion='''Elemento no metálico, símbolo I, número atómico 53, masa atómica relativa 126.904, el más 
pesado de los halógenos (halogenuros) que se encuentran en la naturaleza. En condiciones normales, el yodo es 
un sólido negro, lustroso, y volátil; recibe su nombre por su vapor de color violeta. El yodo es más 
electropositivo que los otros halógenos y sus propiedades se modulan por: la debilidad relativa de los 
enlaces covalentes entre el yodo y elementos más electropositivos.'''
Yodo=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Yodo)

#Xenón
Nombre='Xenón'
Simbolo='Xe'
Numero_Atomico=54
Masa_Atomica = '131.3 u'
Periodo=5
Grupo=18
Categoria='Gases Nobles'
Densidad = '3,06 g/ml'
Informacion='''El xenón se utiliza para llenar cierto tipo de lámparas de destello para fotografía que 
producen luz con un buen equilibrio de todos los colores del espectro visible y pueden ser utilizadas 
10 000 veces o más antes de quemarse. Una lámpara de arco llena con xenón da luz intensa semejante al 
arco de carbono; en particular es valiosa en la proyección de películas.'''
Xenón=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Xenón)

#Cesio
Nombre='Cesio'
Simbolo='Cs'
Numero_Atomico=55
Masa_Atomica = '132.9 u'
Periodo=6
Grupo=1
Categoria='Metales alcalinos'
Densidad = '1,90 g/ml'
Informacion='''El más pesado de los metales alcalinos en el grupo IA de la tabla periódica, a excepción 
del francio, miembro radiactivo de la familia de los metales alcalinos. El cesio es un metal blando, 
ligero y de bajo punto de fusión. Es el más reactivo de los metales alcalinos y en realidad es el menos 
electronegativo y el más reactivo de todos los elementos.'''
Cesio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cesio)

#Bario
Nombre='Bario'
Simbolo='Ba'
Numero_Atomico=56
Masa_Atomica = '137.3 u'
Periodo=6
Grupo=2
Categoria='Alcalinotérreos'
Densidad = '3,5 g/ml'
Informacion='''El bario ocupa el decimoctavo lugar en abundancia en la corteza terrestre, en donde se 
encuentra en un 0.04%, valor intermedio entre el calcio y el estroncio, los otros metales alcalinotérreos. 
Los compuestos de bario se obtienen de la minería y por conversión de dos minerales de bario. '''
Bario=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Bario)

#Latano
Nombre='Latano'
Simbolo='La'
Numero_Atomico=57
Masa_Atomica = '138.9 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '6.18 g/ml'
Informacion='''El lantano es un metal blando, maleable, dúctil y de color blanco plateado. El lantano se encuentra 
de forma natural en los sedimentos: se oxida rápidamente en el aire y reacciona con el agua para formar el hidróxido. 
La sal 1:1 de fosfato de lantano (LaPO4) tiene una solubilidad extremadamente baja en el agua, Del mismo modo, 
el carbonato de lantano (La2(CO3)3) también tiene una solubilidad en el agua muy baja, 1,02 x 10-7 mol/L,
 calculada a partir del Ksp de 4 x 10-34 mol5/L5 a 25°C y I = 0 mol/dm3 informado por Martell & Smith (1974)'''
Latano=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Latano)

#Cerio
Nombre='Cerio'
Simbolo='Ce'
Numero_Atomico=58
Masa_Atomica = '140.1 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '6,67 g/ml'
Informacion='''Es el elemento metálico más abundante del grupo de las tierras raras en la tabla periódica. 
El elemento natural está constituido de los isótopos 136Ce, 138Ce, 140Ce y 142Ce. El 142Ce radiactivo 
tiene una vida media de 5 x 1015 años. El cerio se encuentra mezclado con otras tierras raras en muchos 
minerales, en particular en monacita y blastnasita y también se halla entre los productos de la fisión 
de uranio, torio y plutonio.'''
Cerio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Cerio)

#Praseodimio
Nombre='Praseodimio'
Simbolo='Pr'
Numero_Atomico=59
Masa_Atomica = '140.9 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '6,77 g/ml'
Informacion='''El praseodimio es un elemento metálico del grupo de las tierras raras. El isótopo estable 140.907 
corresponde al 100 porciento del elemento presente en la naturaleza. El óxido es un polvo negro cuya composición 
varía según el método de preparación. Si se oxida bajo una presión alta de oxígeno puede aproximarse a la composición PrO2. 
El óxido negro se disuelve en ácido con liberación de oxígeno para dar soluciones verdes o sales verdes que tienen 
aplicación en la industria de la cerámica para colorear esmaltes y vidrios.'''  
Praseodimio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Praseodimio)

#Neodimio
Nombre='Neodimio'
Simbolo='Nd'
Numero_Atomico=60
Masa_Atomica = '144.2 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '7 g/ml'
Informacion='''Se encuentra en la naturaleza en seis isótopos. El óxido, Nd2O3, es un polvo azul claro. Se disuelve 
en ácidos minerales para dar soluciones violeta rojizas. El neodimio fue descubierto por Carl F. Auer von Welsbach, 
un científico alemán, en 1885. Separó neodimio, así como el elemento praseodimio, de un material conocido como didimio. '''
Neodimio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Neodimio)

#Prometio
Nombre='Prometio'
Simbolo='Pm'
Numero_Atomico=61
Masa_Atomica = '147 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '- g/ml'
Informacion='''Aunque algunos científicos han reclamado haber descubierto este elemento en la naturaleza tras la observación 
de ciertas líneas espectrales, nadie ha podido aislar el elemento 61 de materiales que se presentan en la naturaleza. 
Se produce artificialmente en los reactores nucleares, ya que es uno de los elementos que resulta de la fisión 
del uranio, torio y plutonio.'''
Prometio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Prometio)

#Samario
Nombre='Samario'
Simbolo='Sm'
Numero_Atomico=62
Masa_Atomica = '150.3 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '7,54 g/ml'
Informacion='''El óxido de samario es de color amarillo pálido; muy soluble en la mayor parte de los ácidos, 
dando sales amarillo-topacio en solución. El samario tiene un empleo limitado en la industria cerámica y se 
utiliza como catalizador en ciertas reacciones orgánicas. Uno de sus isótopos tiene una superficie grande para la 
captura de neutrones, por lo que es de gran interés en la industria atómica como barra de control y envenenamientos nucleares.'''
Samario=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Samario)

#Europio
Nombre='Europio'
Simbolo='Eu'
Numero_Atomico=63
Masa_Atomica = '152 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '5,26 g/ml'
Informacion='''Los isótopos estables, 151Eu y 153Eu, son naturales. El metal es el segundo más volátil de las tierras raras y 
tiene una presión de vapor considerable en su punto de fusión. Es muy blando, y es atacado rápidamente por el aire; en realidad 
pertenece más bien a la serie del calcio-estroncio-bario que a las tierras raras.'''
Europio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Europio)

#Gadolinio
Nombre='Gadolinio'
Simbolo='Gd'
Numero_Atomico=64
Masa_Atomica = '157.2 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '7,89 g/ml'
Informacion='''El elemento natural está compuesto de ocho isótopos. Se llama así en honor del científico sueco J. Gadolin. 
El óxido, Gd2O3, en forma de polvo, es blanco y las soluciones de sus sales son incoloras. El gadolinio metálico es 
paramagnético y se vuelve fuertemente ferromagnético a temperaturas inferiores a la ambiente. El punto Curie 
donde ocurre esta transición es de unos 16 K.'''      
Gadolinio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Gadolinio)

#Terbio
Nombre='Terbio'
Simbolo='Tb'
Numero_Atomico=65
Masa_Atomica = '158.9 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '8,27 g/ml'
Informacion='''El óxido común, Tb4O7, es de color café y se obtiene cuando sus sales se calientan en aire. 
Todas sus sales son trivalentes y de color blanco; cuando se disuelven, dan soluciones incoloras. Los óxidos 
mayores se descomponen lentamente cuando son tratados con ácido diluido para dar iones trivalentes en solución. 
Aunque el metal es atacado fácilmente a temperaturas altas por el aire, el ataque es muy lento a la temperatura 
ambiente. El metal, tiene un punto de Néel cercano a 229 K y un punto Curie cercano a 220 K.''' 
Terbio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Terbio)

#Disprocio
Nombre='Disprocio'
Simbolo='Dy'
Numero_Atomico=66
Masa_Atomica = '162.5 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '8,54 g/ml'
Informacion='''El disprosio forma un óxido blanco, Dy2O3 que se disuelve en ácido para producir una solución 
amarillo-verdosa. El metal es atacado con facilidad por el aire a altas temperaturas, pero a la temperatura 
ambiente, en bloques, es bastante estable en la atmósfera y permanece brillante durante largos periodos.'''
Disprocio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Disprocio)

#Holmio
Nombre='Holmio'
Simbolo='Ho'
Numero_Atomico=67
Masa_Atomica = '164.9 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '8,80 g/ml'
Informacion='''Es un elemento metálico colocado en el grupo de las tierras raras. El isótopo estable 165Ho constituye
el 100 porciento del elemento en la naturaleza. El metal es paramagnético, pero a medida que la temperatura 
disminuye se convierte en antiferromagnético y luego al sistema ferromagnético. El holmio fue descubierto 
por Per Theodro Cleve, un químico sueco, en 1879.'''
Holmio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Holmio)

#Erbio
Nombre='Erbio'
Simbolo='Er'
Numero_Atomico=68
Masa_Atomica = '167.3 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '9,05 g/ml'
Informacion='''El elemento natural consta de seis isótopos estables. El óxido rosa Er2O3 se disuelve en ácidos 
minerales para dar soluciones color de rosa. Las sales son paramagnéticas y los iones trivalentes. A temperaturas 
bajas el metal es antiferromagnético y a temperaturas aún más bajas se vuelve fuertemente ferromagnético.'''  
Erbio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Erbio)

#Tulio
Nombre='Tulio'
Simbolo='Tm'
Numero_Atomico=69
Masa_Atomica = '168.9 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '9.33 g/ml'
Informacion='''El isótopo estable 169Tm constituye el 100 porciento del elemento que se encuentra en la naturaleza. 
Las sales de tulio poseen un color verde pálido y sus soluciones toman un ligero tinte verdoso. El metal tiene una 
elevada presión de vapor en el punto de fusión. Cuando el 169Tm es irradiado en un reactor nuclear se forma 170Tm. 
El isótopo emite fuertes rayos X de 84 KeV, y este material se utiliza para fabricar pequeñas unidades 
portátiles de rayos X que se usan en medicina.'''
Tulio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Tulio)

#Iterbio
Nombre='Iterbio'
Simbolo='Yb'
Numero_Atomico=70
Masa_Atomica = '173 u'
Periodo=6
Grupo=3
Categoria='Lantanidos'
Densidad = '6,98 g/ml'
Informacion='''El óxido más común, Yb2O3, es incoloro y se disuelve fácilmente en ácidos para formar soluciones 
incoloras de sales trivalentes, que son paramagnéticas. El iterbio produce también una serie de compuestos divalentes; 
las sales divalentes son solubles en agua pero reaccionan muy lentamente liberando hidrógeno.'''        
Iterbio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Iterbio)

#Lutecio
Nombre='Lutecio'
Simbolo='Lu'
Numero_Atomico=71
Masa_Atomica = '175 u'
Periodo=6
Grupo=3
Categoria='Metales de transición'
Densidad = '9,84 g/ml'
Informacion='''El lutecio, junto con el itrio y el lantano, es de interés para los científicos que estudian 
el magnetismo. Estos tres elementos sólo forman iones trivalentes con subcapas que se han completado, por lo 
que no tienen electrones desapareados para contribuir al magnetismo. Su radio es muy parecido al de otros 
iones o metales de las tierras raras y forma soluciones de sólidos o mezclas de cristales con los elementos 
fuertemente magnéticos de las tierras raras en casi todas las composiciones.'''
Lutecio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Lutecio)

#Hafnio
Nombre='Hafnio'
Simbolo='Hf'
Numero_Atomico=72
Masa_Atomica = '178.5 u'
Periodo=6
Grupo=4
Categoria='Metales de transición'
Densidad = '13,1 g/ml'
Informacion='''El hafnio es un metal plateado, lustroso, que se funde cerca de los 2222ºC (4032ºF). El metal 
no tiene aplicaciones excepto en barras de control para reactores nucleares. La química del hafnio es 
casi idéntica a la del zirconio. La semejanza de ambos es una consecuencia de la contracción lantánida, 
la cual lleva a valores de radio iónico casi idénticos. '''
Hafnio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Hafnio)

#Tantalo
Nombre='Tantalio'
Simbolo='Ta'
Numero_Atomico=73
Masa_Atomica = '180.9 u'
Periodo=6
Grupo=5
Categoria='Metales de transición'
Densidad = '16,61 g/ml'
Informacion='''El metal tantalio se emplea en la fabricación de capacitores para equipo electrónico, los cuales 
incluyen radios de banda civil, detectores de humo, marcapasos cardiacos y automóviles. Se utiliza también en 
las superficies para transferencia de calor del equipo de producción en la industria química, en especial 
cuando se tienen condiciones extraordinarias corrosivas. Su inercia química ha hecho que se le hayan encontrado 
aplicaciones dentales y quirúrgicas.'''
Tantalio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Tantalio)

#Volfromio
Nombre='Volframio'
Simbolo='W'
Numero_Atomico=74
Masa_Atomica = '183.8 u'
Periodo=6
Grupo=6
Categoria='Metales de transición'
Densidad = '19,3 g/ml'
Informacion='''Este metal tiene una estructura cúbica centrada en el cuerpo y brillo metálico gris plateado. 
Su punto de fusión de 3410ºC (6170ºF) es el más alto de los metales. El metal exhibe una baja presión de vapor, 
alta densidad y gran fuerza a temperaturas elevadas en ausencia de aire, y es extremadamente duro'''
Volframio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Volframio)

#Renio
Nombre='Renio'
Simbolo='Re'
Numero_Atomico=75
Masa_Atomica = '186.2 u'
Periodo=6
Grupo=7
Categoria='Metales de transición'
Densidad = '21,0 g/ml'
Informacion='''l renio, al igual que su homólogo tecnecio, puede oxidarse a temperaturas elevadas con oxígeno, 
para forma el heptóxido volátil, Re2O7; éste, a su vez, puede reducirse a un óxido menor, ReO2. Los compuestos 
ReO3, Re2O3 y Re2O se conocen bien. El ácido perrénico, HReO4 es un ácido monobásico fuerte y un agente oxidante 
muy débil. También se conocen los complejos perrenatos, como el perrenato hexaamina de cobalto [Co(NH3)6(ReO4)3].'''
Renio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Renio)

#Osmio
Nombre='Osmio'
Simbolo='Os'
Numero_Atomico=76
Masa_Atomica = '190.2 u'
Periodo=6
Grupo=8
Categoria='Metales de transición'
Densidad = '22,6 g/ml'
Informacion='''El osmio, al igual que otros metales como el platino, es activo catalíticamente. El tetróxido de osmio 
se emplea como reactivo orgánico y colorante para observar tejidos al microscopio. Las aleaciones de osmio con rodio, 
rutenio, iridio o platino se utilizan en plumines de estilográficas, puntas de compases, agujas fonográficas, contactos 
eléctricos y pivotes de instrumentos, debido a su extrema dureza y resistencia a la corrosión.'''
Osmio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Osmio)

#Iridio
Nombre='Iridio'
Simbolo='Ir'
Numero_Atomico=77
Masa_Atomica = '192.2 u'
Periodo=6
Grupo=9
Categoria='Metales de transición'
Densidad = '22,5 g/ml'
Informacion='''El iridio tiene mucha menor resistencia a la oxidación que el platino o el rodio, pero mayor que el rutenio o 
el osmio. Aproximadamente a 600ºC (1110ºF) se forma una fina película de óxido adherente, IrO2. Es el único metal que puede 
utilizarse sin protección al aire hasta 2300ºC (4170ºF), con esperanza de vida. No lo ataca ningún ácido, incluyendo el agua regia, 
posee una fuerte tendencia a formar compuestos de coordinación.'''
Iridio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Iridio)

#Platino
Nombre='Platino'
Simbolo='Pt'
Numero_Atomico=78
Masa_Atomica = '195.1 u'
Periodo=6
Grupo=10
Categoria='Metales de transición'
Densidad = '21,4 g/ml'
Informacion='''Es un metal noble blanco, blando y dúctil. Los metales del grupo del platino ( platino, paladio, 
iridio, rodio , osmio y rutenio) se encuentran ampliamente distribuidos sobre la tierra, pero su dilución extrema 
imposibilita su recuperación, excepto en circunstancias especiales. Los metales del grupo del platino se utilizan 
mucho en el campo de la química a causa de su actividad catalítica y de su baja reactividad. Como catalizador, 
el platino se emplea en las reacciones de hidrogenación, deshidrogenación, isomerización, ciclización, 
deshidratación, deshalogenación y oxidación.'''  
Platino=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Platino)

#Oro
Nombre='Oro'
Simbolo='Au'
Numero_Atomico=79
Masa_Atomica = '197 u'
Periodo=6
Grupo=11
Categoria='Metales de transición'
Densidad = '19,3 g/ml'
Informacion='''Es un metal muy denso, blando y de color amarillo intenso. El oro se clasifica como metal pesado 
y noble; en el comercio es el más común de los metales preciosos. El cobre, la plata y el oro están en el mismo 
grupo en la tabla periódica. La fuente del símbolo químico, Au, es su nombre en latín aurum (amanecer radiante). 
Hay sólo un isótopo estable del oro, con número de masa 197.'''  
Oro=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Oro)

#Mercurio
Nombre='Mercurio'
Simbolo='Hg'
Numero_Atomico=80
Masa_Atomica = '200.6 u'
Periodo=6
Grupo=12
Categoria='Metales de transición'
Densidad = '16,6 g/ml'
Informacion='''Es un líquido blanco plateado a temperatura ambiente (punto de fusión -38.4ºC o -37.46ºF); 
ebulle a 357ºC (675.05ºF) a presión atmosférica. Es un metal noble, soluble únicamente en soluciones oxidantes. 
El mercurio sólido es tan suave como el plomo. El metal y sus compuestos son muy tóxicos. El mercurio forma soluciones 
llamadas amalgamas con algunos metales (por ejemplo, oro, plata, platino, uranio, cobre, plomo, sodio y potasio).'''
Mercurio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Mercurio)

#Talio
Nombre='Talio'
Simbolo='Tl'
Numero_Atomico=81
Masa_Atomica = '204.4 u'
Periodo=6
Grupo=13
Categoria='Metales'
Densidad = '11,85 g/ml'
Informacion='''El talio se encuentra en la corteza terrestre en proporción de 0.00006%, principalmente como compuesto 
minoritario en minerales de hierro, cobre, sulfuros y seleniuros. Los minerales de talio se consideran raros. Tiene un 
empleo importante en los componentes electrónicos; por ejemplo, los cristales de yoduro de sodio, activados por talio y 
usados en tubos fotomultiplicadores. También se utiliza en aleaciones de bajo punto de fusión, lentes ópticas y sellos 
de vidrio para almacenar componentes electrónicos.'''       
Talio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Talio)

#Plomo
Nombre='Plomo'
Simbolo='Pb'
Numero_Atomico=82
Masa_Atomica = '207.2 u'
Periodo=6
Grupo=14
Categoria='Metales'
Densidad = '11,4 g/ml'
Informacion='''El plomo es un metal pesado (densidad relativa, o gravedad específica, de 11.4 s 16ºC (61ºF)), de color azuloso, 
que se empaña para adquirir un color gris mate. Es flexible, inelástico, se funde con facilidad, se funde a 327.4ºC (621.3ºF) y 
hierve a 1725ºC (3164ºF). Las valencias químicas normales son 2 y 4. Es relativamente resistente al ataque de 
los ácidos sulfúrico y clorhídrico.'''
Plomo=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Plomo)

#Bismuto
Nombre='Bismuto'
Simbolo='Bi'
Numero_Atomico=83
Masa_Atomica = '209.2 u'
Periodo=6
Grupo=15
Categoria='Metales'
Densidad = '9.8 g/ml'
Informacion='''Pertenece al grupo Va de la tabla periódica. Es el elemento más metálico en este grupo, 
tanto en propiedades físicas como químicas. El único isótopo estable es el de masa 209. Se estima que la 
corteza terrestre contiene cerca de 0.00002 porciento de bismuto. Existe en la naturaleza como metal libre 
y en minerales. Los principales depósitos están en Sudamérica, pero en Estados Unidos se obtiene principalmente 
como subproducto del refinado de los minerales de cobre y plomo.'''
Bismuto=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Bismuto)

#Polonio
Nombre='Polonio'
Simbolo='Po'
Numero_Atomico=84
Masa_Atomica = '210 u'
Periodo=6
Grupo=16
Categoria='Metaloides'
Densidad = '9,2 g/ml'
Informacion='''Marie Curie descubrió el radioisótopo 210Po en la pecblenda (uraninita), isótopo que es el 
penúltimo miembro de las series del decaimiento del radio. Todos los isótopos del polonio son radiactivos 
y de vida media corta, excepto los tres emisores alfa, producidos artificialmente. 208Po (2.9 años) y 209Po 
(100 años), y el natural, 210Po (138.4 días).'''
Polonio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Polonio)

#Astato
Nombre='Astato'
Simbolo='At'
Numero_Atomico=85
Masa_Atomica = '210 u'
Periodo=6
Grupo=17
Categoria='Hálogenos'
Densidad = '- g/ml'
Informacion='''El ástato es el elemento más pesado del grupo de los halógenos, ocupa el lugar debajo del 
yodo en el grupo VII de la tabla periódica. El ástato es un elemento muy inestable, que existe sólo en formas 
radiactivas de vida corta. Se han preparado unos 25 isótopos mediante reacciones nucleares de transmutación artificial. 
El isótopo con mayor tiempo de vida es el 210At, el cual decae en un tiempo de vida media de sólo 8.3 h. '''
Astato=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Astato)

#Radón
Nombre='Radón'
Simbolo='Rn'
Numero_Atomico=86
Masa_Atomica = '222 u'
Periodo=6
Grupo=18
Categoria='Gases Nobles'
Densidad = '- g/ml'
Informacion=''' El radón es una emanación gaseosa producto de la desintegración radiactiva del radio. 
Es muy radiactivo y se desintegra con la emisión de partículas energéticas alfa. Es el elemento más 
pesado del grupo de los gases nobles, o inertes, y, por tanto, se caracteriza por su inercia química. 
Todos sus isótopos son radiactivos con vida media corta.'''
Radón=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Radón)

#Francio
Nombre='Francio'
Simbolo='Fr'
Numero_Atomico=87
Masa_Atomica = '233 u'
Periodo=7
Grupo=1
Categoria='Metales Alcalinos'
Densidad = '- g/ml'
Informacion='''Se distingue por su inestabilidad nuclear, ya que existe sólo en formas radiactivas de vida corta; 
el más estable tiene una vida media de 21 minutos. El principal isótopo del francio es el actinio-K, isótopo de masa 223, 
el cual proviene del decaimiento del actinio radiactivo, de las propiedades conocidas, es muy probable que ninguna forma 
de vida larga del elemento 87 se encuentre en la naturaleza o sintetizada de manera artificial.'''
Francio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Francio)

#Radio
Nombre='Radio'
Simbolo='Ra'
Numero_Atomico=88
Masa_Atomica = '266 u'
Periodo=7
Grupo=2
Categoria='Alcalinotérreos'
Densidad = '5 g/ml'
Informacion=''' El radio es un elemento radiactivo raro, encontrado en minerales de uranio en proporción 
de una parte por aproximadamente 3 millones de partes de uranio. Desde el punto de vista químico, el 
radio es un metal alcalinotérreo y tiene propiedades muy semejantes a las del bario. Biológicamente, 
el radio se concentra en los huesos al reemplazar al calcio y, tras una irradiación prolongada, 
causa anemia y neoplasias cancerosas.'''
Radio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Radio)

#Actinio
Nombre='Actinio'
Simbolo='Ac'
Numero_Atomico=89
Masa_Atomica = '227 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '10.07 g/ml'
Informacion='''El actinio es un elemento metálico radiactivo plateado. El actinio brilla en la oscuridad 
debido a su intensa radiactividad con una luz azul.  El actinio fue descubierto en 1899 por André-Louis 
Debierne, un químico francés, que lo separó de la pechblenda. Friedrich Otto Giesel descubrió el actinio 
de forma independiente en 1902. El comportamiento químico del actinio es similar al de la tierra rara lantano. '''
Actinio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Actinio)

#Torio
Nombre='Torio'
Simbolo='Th'
Numero_Atomico=90
Masa_Atomica = '232 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '11,7 g/ml'
Informacion='''Los compuestos de óxido de torio se utilizan en la producción de mantas de gas incandescentes. 
El óxido de torio se ha empleado también incorporado al tungsteno metálico, y sirve para producir filamentos 
para lámparas eléctricas. Se emplea en catalizadores para facilitar ciertas reacciones de química orgánica y 
tiene aplicaciones especiales como material cerámico de alta temperatura. El metal o sus óxidos se utilizan 
en algunas lámparas electrónicas, fotoceldas y electrodos especiales para soldadura.'''
Torio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Torio)

#Protactinio
Nombre='Protactinio'
Simbolo='Pa'
Numero_Atomico=91
Masa_Atomica = '231 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '15,4 g/ml'
Informacion='''Los isótopos con número de masa 216, 217 y 222-238 son radiactivos. Sólo 231Pa, 234Pa y 234mPa 
están presentes en la naturaleza. El más importante de ellos es el 231Pa, emisor alfa con una vida media de 32 500 años. 
El isótopo artificial 233Pa es intermediario importante en la producción del 233U fisionable. Tanto el 231Pa como el 
233Pa pueden sintetizarse por irradiación neutrónica del torio.'''
Protactinio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Protactinio)

#Uranio
Nombre='Uranio'
Simbolo='U'
Numero_Atomico=92
Masa_Atomica = '238 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '18,95 g/ml'
Informacion='''El uranio es una mezcla de tres isótopos: 234U,235U y238U. Se cree que está localizado principalmente 
en la corteza terrestre, donde la concentración promedio es 4 partes por millón (ppm). El contenido total en la 
corteza terrestre hasta la profundidad de 25 Km (15 mi) se calcula en 1017 Kg (2.2 x 1017 lb); los océanos pueden 
contener 1013 Kg (2.2 x 1013 lb) de uranio. Se conocen cientos de minerales que contienen uranio, pero sólo unos 
pocos son de interés comercial.'''
Uranio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Uranio)

#Neptunio
Nombre='Neptunio'
Simbolo='Np'
Numero_Atomico=93
Masa_Atomica = '237 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '20.2 g/ml'
Informacion=''' El neptunio es un miembro de los actínidos o de la serie 
de elementos 5f. Fue sintetizado como el primer elemento transuránico en 
1940 por bombardeo de uranio con neutrones para producir neptunio 239. Desde el punto de vista químico es importante el isótopo más ligero 237Np, 
emisor alfa de larga vida, con una vida media de 2.14 x 106 años.'''     
Neptunio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Neptunio)

#Plutonio
Nombre='Plutonio'
Simbolo='Pu'
Numero_Atomico=94
Masa_Atomica = '242 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion='''Es un metal plateado, reactivo, de la serie de los actínidos. El isótopo principal de interés 
químico es 239Pu, que tiene una vida media de 24 131 años. Se forma en los reactores nucleares. El plutonio-239 
es fisionable, pero puede capturar también neutrones para formar isótopos superiores de plutonio.'''
Plutonio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Plutonio)

#Americio
Nombre='Americio'
Simbolo='Am'
Numero_Atomico=95
Masa_Atomica = '243 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '11,7 g/ml'
Informacion='''El isótopo 241Am es emisor de partículas alfa, con una vida promedio de 433 años. Los otros 
isótopos del americio incluyen desde la masa 232 hasta la 247, pero sólo los isótopos de masas 241 y 243 son 
importantes. El isótopo 241Am se prepara comúnmente a partir de plutonio y se vende para varios usos industriales, 
entre ellos como fuente de radiaciones gamma de 59 KeV y como componente en fuentes de neutrones.'''    
Americio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Americio)

#Curio
Nombre='Curio'
Simbolo='Cm'
Numero_Atomico=96
Masa_Atomica = '247 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion=''' El curio no existe en el ambiente terrestre, pero puede producirse en forma artificial. 
Sus propiedades químicas se parecen tanto a las de las tierras raras típicas que, si no fuera por su radiactividad, 
podría con facilidad confundirse fácilmente con uno de estos elementos. Entre los isótopos conocidos del 
curio figuran los de número de masa 238 a 250.'''
Curio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Curio)

#Berquelio
Nombre='Berquelio'
Simbolo='Bk'
Numero_Atomico=97
Masa_Atomica = '247 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion='''El berkelio no se encuentra en la corteza terrestre por no tener isótopos estables. Debe prepararse 
por reacciones nucleares usando elementos blancos más abundantes. Estas reacciones incluyen bombardeo con partículas 
cargadas, irradiación con neutrones de reactores de alto flujo o producción en un dispositivo termonuclear.'''
Berquelio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Berquelio)

#Californio
Nombre='Californio'
Simbolo='Cf'
Numero_Atomico=98
Masa_Atomica = '251 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion='''Su descubrimiento y producción se basa en la transmutación nuclear artificial de isótopos radiactivos 
de elementos más ligeros. Todos los isótopos del californio son radiactivos, con intervalo de vidas medias entre un 
minuto y unos 1000 años. Por su inestabilidad nuclear el californio no existe en la corteza terrestre.'''
Californio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Californio)

#Einstenio
Nombre='Einstenio'
Simbolo='Es'
Numero_Atomico=99
Masa_Atomica = '252 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion='''No se encuentra en la naturaleza, sino que se obtiene de manera artificial por transmutación nuclear 
de elementos más ligeros. Todos los isótopos del einstenio son radiactivos, con vida media que abarca de unos pocos 
segundos hasta cerca de un año.'''
Einstenio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Einstenio)

#Fermio
Nombre='Fermio'
Simbolo='Fm'
Numero_Atomico=100
Masa_Atomica = '257 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion='''El undécimo elemento de los actínidos. El fermio no se encuentra en la naturaleza; su descubrimiento 
y producción se alcanza por transmutación nuclear artificial de elementos más ligeros. Se han descubierto los isótopos 
radiactivos de número de masa 244-259. El peso total del fermio que ha sido sintetizado es mucho menor 
de una millonésima de gramo.'''
Fermio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Fermio)

#Mendelevio
Nombre='Mendelevio'
Simbolo='Md'
Numero_Atomico=101
Masa_Atomica = '256 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion=''' El mendelevio no se encuentra en la naturaleza; fue descubierto y se prepara por transmutación 
nuclear artificial de un elemento más ligero. Sus isótopos conocidos tienen números de masa de 248 a 258 y 
vidas medias que comprenden unos pocos segundos hasta aproximadamente 55 días. Todos se producen al bombardear 
partículas cargadas de los isótopos más abundantes.'''
Mendelevio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Mendelevio)

#Nobelio
Nombre='Nobelio'
Simbolo='No'
Numero_Atomico=102
Masa_Atomica = '259 u'
Periodo=7
Grupo=3
Categoria='Latanidos'
Densidad = '- g/ml'
Informacion=''' Es un elemento sintético producido en el laboratorio. Su decaimiento se realiza por emisión 
de partículas alfa, es decir, un ion de helio doblemente cargado. Hasta la fecha sólo se han producido cantidades 
atómicas del elemento. El nobelio es el décimo elemento más pesado que el uranio producido sintéticamente y el 
decimotercer miembro de los actínidos, serie de elementos parecidos a las tierras raras.'''
Nobelio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Nobelio)

#Laurencio
Nombre='Laurencio'
Simbolo='Lr'
Numero_Atomico=103
Masa_Atomica = '262 u'
Periodo=7
Grupo=3
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Se han determinado las propiedades nucleares de todos los isótopos del laurencio de masa 255 a 260. 
El 260Lr es un emisor alfa con un promedio de vida de 3 minutos y por ello es el isótopo de vida más larga que se conoce.'''
Laurencio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Laurencio)

#Rutherfordio
Nombre='Rutherfordio'
Simbolo='Rf'
Numero_Atomico=104
Masa_Atomica = '261.1 u'
Periodo=7
Grupo=4
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Primer elemento después de la serie de los actínidos y el duodécimo elemento transuránico. 
En 1964 G. N. Flerov y colaboradores, en los laboratorios Dubna de la Unión Soviética, declararon ser los primeros 
en presentar la identificación del elemento 104, y un poco después sugirieron el nombre de Kurchatovio (símbolo Ku). 
El grupo de Dubna reclamó la preparación del elemento 104, número de masa 260, irradiando plutonio-242, con iones neón-22.'''
Rutherfordio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Rutherfordio)

#Dubnio
Nombre='Dubnio'
Simbolo='Db'
Numero_Atomico=105
Masa_Atomica = '262.1 u'
Periodo=7
Grupo=5
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Elemento químico sintetizado e identificado sin lugar a duda por primera vez por A. Ghiorso 
y colegas en marzo de 1970 en el Laboratorio de Radiación Lawrence, Berkeley (California), en el acelerador 
lineal de iones pesados (HILAC).'''
Dubnio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Dubnio)

#Seaborgio
Nombre='Seaborgio'
Simbolo='Sg'
Numero_Atomico=106
Masa_Atomica = '263.1 u'
Periodo=7
Grupo=6
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Sintetizado e identificado en 1974; es el decimocuarto de los elementos transuránicos sintéticos. 
El descubrimiento del Seaborgio tuvo lugar casi simultáneamente en dos laboratorios nucleares muy distantes: 
el Lawrence de Berkeley, en la Universidad de California, y el Instituto Conjunto de Investigación Nuclear de 
Dubna (cerca de Moscú). Se usaron dos aproximaciones diferentes e independientes en esta difícil realización, 
en que se bombardeó con iones pesados.'''
Seaborgio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Seaborgio)

#Bohrio
Nombre='Bohrio'
Simbolo='Bh'
Numero_Atomico=107
Masa_Atomica = '264.1 u'
Periodo=7
Grupo=7
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Elemento químico que se espera que tenga propiedades químicas semejantes a las del elemento renio. 
Fue sintetizado e identificado sin ambigüedad en 1981 por un equipo de Darmstadt, Alemania, equipo dirigido por P. 
Armbruster y G. Müzenberg. La reacción usada para producir el elemento fue propuesta y aplicada en 1976 por un 
grupo de Dubna (cerca de Moscú), que estaba bajo la guía de Yu. Organessian. Un blanco de 209Bi fue bombardeado 
por un haz de proyectiles de 54Cr.'''
Bohrio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Bohrio)

#Hassio
Nombre='Hassio'
Simbolo='Hs'
Numero_Atomico=108
Masa_Atomica = '277 u'
Periodo=7
Grupo=8
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Elemento químico que se espera tenga propiedades químicas similares a las del elemento osmio. 
Fue sintetizado e identificado en 1984 en Darmstadt, Alemania, por el mismo equipo que identificó por primera 
vez los elementos Bh y Mt. El isótopo 265Hs fue producido en una reacción de fusión bombardeando un blanco de 
208Pb con un haz de proyectiles de 58Fe. Las mismas técnicas experimentales se emplearon en la búsqueda de 
los elementos Bh y Mt.'''
Hassio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Hassio)

#Meitnerio
Nombre='Meitnerio'
Simbolo='Mt'
Numero_Atomico=109
Masa_Atomica = '268 u'
Periodo=7
Grupo=9
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Elemento que se espera sea químicamente similar al elemento iridio. Se ha producido un átomo 
y se ha observado su decaimiento en la reacción de fusión entre el 58Fe y el 209Bi. Este experimento fue llevado 
a cabo en 1982 por el mismo equipo alemán que descubrió el elemento Bh, usando las mismas técnicas.'''
Meitnerio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Meitnerio)

#Darmstatio
Nombre='Darmstatio'
Simbolo='Ds'
Numero_Atomico=110
Masa_Atomica = '271 u'
Periodo=7
Grupo=10
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''Es un elemento sintetico que decae rapidamente. Los isotoposde masa 279-281 tienen una vidad 
media de microsegundos'''
Darmstatio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Darmstatio)

#Roentgenio
Nombre='Roentgenio'
Simbolo='Rg'
Numero_Atomico=111
Masa_Atomica = '272 u'
Periodo=7
Grupo=11
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''-'''
Roentgenio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Roentgenio)

#Copernicio
Nombre='Copernicio'
Simbolo='Cn'
Numero_Atomico=112
Masa_Atomica = '285 u'
Periodo=7
Grupo=12
Categoria='Metales de transición'
Densidad = '- g/ml'
Informacion='''-'''
Copernicio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Copernicio)

#Nihonio
Nombre='Nihonio'
Simbolo='Nh'
Numero_Atomico=113
Masa_Atomica = '284 u'
Periodo=7
Grupo=13
Categoria='Metales'
Densidad = '- g/ml'
Informacion='''-'''
Nihonio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Nihonio)

#Flerevio
Nombre='Flerevio'
Simbolo='Fl'
Numero_Atomico=114
Masa_Atomica = '289 u'
Periodo=7
Grupo=14
Categoria='Metales'
Densidad = '- g/ml'
Informacion='''-'''
Flerevio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Flerevio)

#Moscovio
Nombre='Moscovio'
Simbolo='Mc'
Numero_Atomico=115
Masa_Atomica = '288 u'
Periodo=7
Grupo=15
Categoria='Metales'
Densidad = '- g/ml'
Informacion='''-'''
Moscovio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Moscovio)

#Livermorio
Nombre='Livermorio'
Simbolo='Lv'
Numero_Atomico=116
Masa_Atomica = '292 u'
Periodo=7
Grupo=16
Categoria='Metales'
Densidad = '- g/ml'
Informacion='''-'''
Livermorio=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Livermorio)

#Teneso
Nombre='Teneso'
Simbolo='Ts'
Numero_Atomico=117
Masa_Atomica = '294 u'
Periodo=7
Grupo=17
Categoria='Halógenos'
Densidad = '- g/ml'
Informacion='''-'''
Teneso=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Teneso)

#Oganesón
Nombre='Oganesón'
Simbolo='Og'
Numero_Atomico=118
Masa_Atomica = '294 u'
Periodo=7
Grupo=18
Categoria='Gases Nobles'
Densidad = '- g/ml'
Informacion='''-'''
Oganesón=Elemento(Nombre,Simbolo,Numero_Atomico,Masa_Atomica,Periodo,Grupo,Densidad,Categoria,Informacion)
ListaElementos.append(Oganesón)

def LiEle():
    return ListaElementos