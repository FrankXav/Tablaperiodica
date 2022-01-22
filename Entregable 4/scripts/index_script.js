/*const response = fetch('https://tabalperiodicafrank.herokuapp.com/elemento/list/');
const myinfo = response.json()  */

let relemento, elemento, conteiner, elementoConteiner, numeros, letraElemento, na, ma, nombre

/* const info = async () => {
    relemento = await fetch('https://tabalperiodicafrank.herokuapp.com/elemento/detail/Hidrogeno/')
    elemento = await relemento.json()
    conteiner = document.getElementById('Hidrogeno')
    elementoConteiner = document.createElement('div')
    numeros = document.createElement('div')
    numeros.classList.add('num')
    letraElemento = document.createElement('div')
    letraElemento.classList.add('Letra')
    letraElemento.innerHTML = elemento.simbolo
    na = document.createElement('div')
    na.innerHTML = elemento.no_atomico
    ma = document.createElement('div')
    ma.innerHTML = elemento.masa_atomica.toFixed(2)
    nombre = document.createElement('div')
    nombre.classList.add('Nombre')
    nombre.innerHTML = elemento.nombre
    conteiner.appendChild(elementoConteiner)
    elementoConteiner.appendChild(numeros)
    elementoConteiner.appendChild(letraElemento)
    elementoConteiner.appendChild(nombre)
    numeros.appendChild(na)
    numeros.appendChild(ma)
}*/

const info = async () => {
    const response = await fetch('https://tabalperiodicafrank.herokuapp.com/elemento/list/');
    const myinfo = await response.json()
    console.log(myinfo)
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


info()

 
