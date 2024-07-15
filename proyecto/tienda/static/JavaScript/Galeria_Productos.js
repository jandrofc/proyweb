

/*
Las funciones async en JavaScript son utilizadas para trabajar con operaciones asíncronas,
es decir, operaciones que pueden no completarse inmediatamente, como las solicitudes a una API,
la lectura de archivos, las operaciones de base de datos, etc.

Cuando marcas una función con la palabra clave async, esto significa que la función siempre devolverá una promesa.
Las promesas son objetos que representan el estado final de una operación asíncrona.

El uso de async y await hace que el código asíncrono sea más fácil de leer y escribir. 
await sólo puede ser usado dentro de una función async y hace que la ejecución de la función se pause hasta que la 
promesa se resuelva.
*/

//Leer archivo en servidor local

/*
async function leerArchivo() { //funcion que lee el archivo productos.json y devuelve un mensaje
    //leer un archivo JSON en el navegador, puedes hacerlo utilizando la API Fetch
    
    return fetch('../Json productos/Productos.json')        
    //
    
        .then(response => {  //despues de resivir la respuesta de fetch, ejecuta una pequeña funcion que verifica si la respuesta esta bien o arrojo error
            if (!response.ok) {  //si la respuesta no esta bien, arroja un error
                console.log(response); //muestra en consola la respuesta 
                throw new Error("HTTP error " + response.status); //arroja un error en formato xhr
            }
            return response.json(); //si la respuesta esta bien, devuelve el archivo
        })
        .catch(function() {   //si hay un error en la lectura del archivo al principio, devolvera un mensaje de error y no se caera el programa
            console.log("Error al leer el archivo JSON.");
        });


}
*/


//MOSTRAR Y OCULATAR EL FORMULARIO

function MostrarFormulario(){
    
    var formulario = document.getElementById("formulario");
    var fondo = document.getElementById("fondo-formulario");

    if (formulario.style.display === "" || formulario.style.display === "none") {
        formulario.style.display = "block";
        fondo.style.display = "flex";
        document.set
    }
    else {
        formulario.style.display = "none";
        fondo.style.display = "none";
    }

}
function OcultarFormulario(){
    var formulario = document.getElementById("formulario");
    var fondo = document.getElementById("fondo-formulario");
    formulario.style.display = "none";
    fondo.style.display = "none";
}

//VALIDAR FORMULARIO

function ValidarFormulario(){
    

    
    
    var Nombre = document.getElementById("nombre").value;
    var Categoria = document.getElementById("categoria").value;
    var Producto = document.getElementById("producto").value;
    var opinion = document.getElementById("opinion").value;


    let fullstars = document.querySelectorAll('.bi-star-fill'); //fullstars es un arreglo con los elementos de clase bi-star-fill, estrellas llenas





    if (Nombre=="" || Nombre==null || Nombre==undefined){
        document.getElementById("Mensaje").innerHTML="Ingrese su <span style='font-weight: bold'>Nombre</span> <br>";
        return false;
    }
    else if (Categoria=="" || Categoria==null || Categoria==undefined){
        document.getElementById("Mensaje").innerHTML="Seleccione una <span style='font-weight: bold'>categoria</span> <br>";
        return false;
    }
    else if (Producto=="" || Producto==null || Producto==undefined){
        document.getElementById("Mensaje").innerHTML="Seleccione un <span style='font-weight: bold'>producto</span> <br>";
        return false;
    }
    else if (fullstars[0].style.display === "" || fullstars[0].style.display === "none"){
        document.getElementById("Mensaje").innerHTML="Califique el producto con <span style='font-weight: bold'>estrellas</span> <br>";
        return false;
    }
    else if (opinion=="" || opinion==null || opinion==undefined){
        document.getElementById("Mensaje").innerHTML="Ingrese su <span style='font-weight: bold'>opinion</span> <br>";
        return false;
    }
    else{
        document.getElementById("Mensaje").innerHTML=''
        return true;
    }
    
}




function guardarFormulario(e) {
    
    if (ValidarFormulario()==true){
        alert("Formulario enviado");
        return true;
    }
    else{
        e.preventDefault();
        return false;
    }
}






//CAMBIAR CALIFICACION DE ESTRELLAS

// Obtén todas las estrellas
let stars = document.querySelectorAll('.bi-star'); //stars es un arreglo con los elementos de clase bi-star, estrellas vacias

let fullstars = document.querySelectorAll('.bi-star-fill'); //fullstars es un arreglo con los elementos de clase bi-star-fill, estrellas llenas
stars.forEach((star, index) => { // Agrega un event listener a cada estrella, star es la estrella clickeada como elemento e index la posicion de la estrella en el arreglo
    star.addEventListener('click', () => { //al detectar un click hara lo de abajo
        // Colorea todas las estrellas hasta la que fue clickeada
        for(let i = 0; i <= index; i++) { //recorre todas las estrellas hasta la clickeada, de izquierda a derecha borra las vacias y pone las llenas, la cantidad de estrellas correspondientes
            stars[i].style.display = "none"; //oculta la estrella vacia
            fullstars[i].style.display = "inline-block"; //muestra la estrella llena
        }
    });
});
fullstars.forEach((fullstar, index) => { // Agrega un event listener a cada estrella llenada
    fullstar.addEventListener('click', () => { //al hacer el click hara lo de abajo
        // descolorea todas las estrellas hasta la despues de la clickeada
        for(let i = index+1; i < 5; i++) { //recorre las estrellas desde despues de la clickeada, termina hasta que termine todas las estrellas, el tamaño del arreglo es 5 pero empieza en 0, por eso determinamos hasta 4
            stars[i].style.display = "inline-block"; //muestra la estrella vacia
            fullstars[i].style.display = "none"; //oculta la estrella llena
        }
    });
});



//LEER API PERSONAL DE PRODUCTOS Y SU CATEGORIA Y MOSTRARLOS EN EL FORMULARIO


async function leerArchivo() { //funcion que lee el archivo productos.json y devuelve un mensaje
    //leer un archivo JSON en el navegador, puedes hacerlo utilizando la API Fetch
    
    const url = "https://gist.githubusercontent.com/Nechaiter/f9282b10217392ebccc5dc95cf798714/raw/b35c00862ff9325efa5a952120345dfbd3d26368/Productos.json";
    const obtener = 'get'; // hacemos un metodo para solicitar cosas
    // llamas a api lista de regiones
    
    
    const respuesta_api = await fetch(url, { //  solicitamos el estado de la respuesta, y se espera a obtener antes de seguir con el code
        method: obtener,
    })
    try{
        if (respuesta_api.status!=200){
            console.log(respuesta_api); //debug
            throw new Error("HTTP error " + respuesta_api.status);
        }
        console.log(`Respuesta: ${respuesta_api.status}`) //debug
        return respuesta_api.json(); 
    }
    catch(respuesta_api) {   //si hay un error en la lectura del archivo al principio, devolvera un mensaje de error y no se caera el programa
        console.log("Error al leer el archivo JSON.");
    };

}


function ComprobarSelect(){    //comprueba que categoria esta seleccionada, y si está la opcion cargada de la funcion mostrarProducto
    let categoria_select=document.getElementById("categoria").value;
    if (categoria_select=="" || categoria_select==null || categoria_select==undefined){
        console.log("Categoria no seleccionada");
        return false;
    }else{
        console.log("Categoria seleccionada");
        console.log(categoria_select);
        return true;
    }
    
}


async function MostrarProducto() {  //funcion que muestra los productos solo si hay una categoria seleccionada
    try{
        if (ComprobarSelect()==true){
            const basedatos = await leerArchivo() //espera a que la funcion leerArchivo termine y guarde el archivo en la variable basedatos
            htmlProducto=`<option value="" selected="" disabled="">Escoja su Producto</option>`;
            i=document.getElementById("categoria").value;
            for (let j = 0; j < basedatos.Productos[i].Tipo.length; j++) {
                htmlProducto=htmlProducto+`<option value="${j}">${basedatos.Productos[i].Tipo[j]}</option>`;
                console.log(basedatos.Productos[i].Tipo[j]); //debug
            }
            document.getElementById("producto").innerHTML=htmlProducto;
        }


    } catch (basedatos){}; //si hay un error en la lectura del archivo, se mostrara un mensaje de error de la funcion leerArchivo
}
async function MostrarCategoria() {  //funcion que muestra las categorias, solo si no hay una categoria seleccionada
    try{
        if (ComprobarSelect()==false){
            const basedatos = await leerArchivo() //espera a que la funcion leerArchivo termine y guarde el archivo en la variable basedatos
            htmlCategoria=`<option value="" selected="" disabled="">Escoja la categoria</option>`;
            document.getElementById("producto").innerHTML=`<option value="" selected="" disabled="">Escoja su Producto</option>`
            console.log(basedatos.Productos.length); //debug
            for (let i = 0; i < basedatos.Productos.length; i++) {
                htmlCategoria=htmlCategoria+`<option value="${i}">${basedatos.Productos[i].Categoria}</option>`;
                console.log(basedatos.Productos[i].Categoria); //debug
            }
            document.getElementById("categoria").innerHTML=htmlCategoria;
            console.log(htmlCategoria); //debug
            MostrarProducto();
        }
    }
    catch (basedatos){}
};

let categoria = document.getElementById('categoria'); //selecciona el elemento con id categoria <select>
console.log(document.getElementById('categoria')); //debug
categoria.addEventListener('change', MostrarProducto); //agrega un event listener al elemento de id categoria que al cambiar ejecuta la funcion MostrarProducto <select>


MostrarCategoria(); //llama a la funcion MostrarCategoria

