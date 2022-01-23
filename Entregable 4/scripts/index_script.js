/*const response = fetch('https://tabalperiodicafrank.herokuapp.com/elemento/list/');
const myinfo = response.json()  */

let relemento, elemento, conteiner, elementoConteiner, numeros, letraElemento, na, ma, nombre

const imagen = async (nomele) => {
    link = 'https://tabalperiodicafrank.herokuapp.com/elemento/detail/' + nomele
    relemento = await fetch(link)
    elemento = await relemento.json()
    conteiner = document.getElementById('imagenh')
    conteiner.innerHTML = ""
    /* console.log(elemento.categoria.replace(/ /g, "")) */
    elementoConteiner = document.createElement('div')
    elementoConteiner.classList.add(elemento.categoria.replace(/ /g, ""))
    numeros = document.createElement('div')
    numeros.classList.add('numi')
    nombrenumeros = document.createElement('div')
    nombrenumeros.classList.add('nombresNumi')
    textona=document.createElement('div')
    textona.innerHTML = 'No. Atomico'
    textoma=document.createElement('div')
    textoma.innerHTML = 'Masa Atomica'
    letraElemento = document.createElement('div')
    letraElemento.classList.add('Letrai')
    letraElemento.innerHTML = elemento.simbolo 
    nombreSimbolo = document.createElement('div')
    nombreSimbolo.innerHTML = 'Simbolo'
    na = document.createElement('div')
    na.innerHTML = elemento.no_atomico
    ma = document.createElement('div')
    ma.innerHTML = elemento.masa_atomica.toFixed(2)
    nombre = document.createElement('div')
    nombre.classList.add('Nombrei')
    nombre.innerHTML = elemento.nombre
    nombreNombre = document.createElement('div')
    nombreNombre.innerHTML = 'Nombre'
    conteiner.appendChild(elementoConteiner)
    elementoConteiner.appendChild(numeros)
    elementoConteiner.appendChild(nombrenumeros)
    elementoConteiner.appendChild(nombreSimbolo)
    elementoConteiner.appendChild(letraElemento)
    elementoConteiner.appendChild(nombreNombre)
    elementoConteiner.appendChild(nombre)
    numeros.appendChild(na)
    numeros.appendChild(ma)
    nombrenumeros.appendChild(textona)
    nombrenumeros.appendChild(textoma)
}

const info = async () => {
    const response = await fetch('https://tabalperiodicafrank.herokuapp.com/elemento/list/');
    const myinfo = await response.json()
    myinfo.forEach(element =>{
        conteiner = document.getElementById(element.nombre)
        elementoConteiner = document.createElement('div')
        numeros = document.createElement('div')
        numeros.classList.add('num')
        letraElemento = document.createElement('div')
        letraElemento.classList.add('Letra')
        letraElemento.innerHTML = element.simbolo
        na = document.createElement('div')
        na.innerHTML = element.no_atomico
        ma = document.createElement('div')
        ma.innerHTML = element.masa_atomica.toFixed(2)
        nombre = document.createElement('div')
        nombre.classList.add('Nombre')
        nombre.innerHTML = element.nombre
        conteiner.appendChild(elementoConteiner)
        elementoConteiner.appendChild(numeros)
        elementoConteiner.appendChild(letraElemento)
        elementoConteiner.appendChild(nombre)
        numeros.appendChild(na)
        numeros.appendChild(ma)
    })
}

const categorias = async () => {
    const response = await fetch('https://tabalperiodicafrank.herokuapp.com/elemento/categoria/');
    const myinfo = await response.json()
    myinfo.forEach(element =>{
        console.log(element.categoria.replace(/ /g, ""))
        conteiner = document.getElementById(element.categoria.replace(/ /g, "")+ "c")
        cuadro = document.createElement('div')
        cuadro.classList.add('cuadroc')
        categoriaNom=document.createElement('div')
        categoriaNom.classList.add('textoCategorias')
        if (element.categoria == 'Gases Nobles'){
            cuadro.style.backgroundColor = 'rgb(7, 59, 0)';
        }
        else if (element.categoria == 'Metales de transición'){
            cuadro.style.backgroundColor = 'rgb(3, 131, 190)';
        }
        else if (element.categoria == 'Halógenos'){
            cuadro.style.backgroundColor = 'rgb(0, 156, 8)';
        }
        else if (element.categoria == 'Alcalinotérreos'){
            cuadro.style.backgroundColor = 'rgba(255, 238, 0, 0.87)';
        }
        else if (element.categoria == 'No Metales'){
            cuadro.style.backgroundColor = 'rgb(255, 102, 0)';
        }
        else if (element.categoria == 'Metales Alcalinos'){
            cuadro.style.backgroundColor = 'rgb(0, 0, 90)';
        }
        else if (element.categoria == 'Metaloides'){
            cuadro.style.backgroundColor = 'rgb(207, 0, 69)';
        }
        else if (element.categoria == 'Lantanidos'){
            cuadro.style.backgroundColor = 'rgb(219, 215, 150)';
        }
        else if (element.categoria == 'Metales'){
            cuadro.style.backgroundColor = 'rgb(98, 0, 122)';
        }
        else if (element.categoria == 'Actinido'){
            cuadro.style.backgroundColor = 'rgb(150, 205, 219)';
        }
        categoriaNom.innerHTML=element.categoria
        /* cuadro.innerHTML = 'ola' */
        conteiner.appendChild(cuadro)
        conteiner.appendChild(categoriaNom)
        
    })
}

info()

imagen('Hidrogeno')

categorias()

 
