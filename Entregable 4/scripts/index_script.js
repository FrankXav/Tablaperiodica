const getAll = async () => {
    const response = await fetch('http://127.0.0.1:8000/elemento/list');
    const myinfo = await response.json()  

    const conteinder = document.getElementById('disU')

    myinfo.forEach(element => {
        const div = document.createElement('h1')
        div.innerHTML = element.Nombre;
        conteinder.appendChild(div)
    });
}   
