
//------------------------------------------------------------------------------------------------------------------------------
async function leerArchivo() { //funcion que lee el archivo productos.json y devuelve un mensaje
    //leer un archivo JSON en el navegador, puedes hacerlo utilizando la API Fetch
    
    const url = "https://gist.githubusercontent.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd/raw/b8575eb82dce974fd2647f46819a7568278396bd/comunas-regiones.json";
    const obtener = 'get'; // hacemos un metodo para solicitar cosas
    // llamas a api lista de regiones
    
    
    const respuesta_api = await fetch(url, { //  solicitamos el estado de la respuesta, y se espera a obtener los datos antes de seguir con el code
        method: obtener, //llama al metodo de obtener, variable con el comando, en este caso get
    })
    try{  //Creamos un try para que si hay un error en la lectura del archivo, se pueda mostrar un mensaje de error y que no se caiga el programa 
        if (respuesta_api.status!=200){   //si la respuesta no es 200, es decir, la api indico que no se pudo obtener el archivo, se mostrara un mensaje de error dsp
            throw new Error("HTTP error " + respuesta_api.status); //Muestra el porque no se pudo obtener el archivo por parte de la api
        }
        return respuesta_api.json(); //si no hay porblemas, se devuelve el archivo en formato JSON
    }
    catch(respuesta_api) {  //si hay un error en la lectura del archivo por un link caido o etc, y da un error de codigo en la throw o api.json se mostrara un mensaje de error
        console.log("Error al leer el archivo JSON.");
    };

}
    
    


function ComprobarSelect(){    //comprueba que categoria esta seleccionada, y si está la opcion cargada de la funcion mostrarProducto
    let region_select=document.getElementById("Region").value; //obtiene el valor del primer option seleccionado en el elemento select
    if (region_select=="" || region_select==null || region_select==undefined){
        console.log("Region no seleccionada");
        return false;
    }else{
        console.log("Validacion correcta");
        return true;
    }
}


async function MostrarComuna() {  //funcion que muestra los productos solo si hay una categoria seleccionada
    try{
        if (ComprobarSelect()==true){ //comprueba si el usurio selecciono una categoria
            const basedatos = await leerArchivo() //espera a que la funcion leerArchivo termine y guarde el archivo en la variable basedatos
            htmlComuna=`<option value="" selected="" disabled="">Escoja su Comuna</option>`; //muestra el mismo placeholder que se sobreescribira sobre el otro de la funcion MostrarRegion
            let regionString=document.getElementById("Region").value; //obtiene el valor del primer option seleccionado en el elemento , obtiene el nombre de la region
            const regionIndex=ArrayRegion.indexOf(regionString); //obtenemos el indice de la region seleccionada en el array de regiones para usarlo en la base de datos
            
            for (let j = 0; j < basedatos.regiones[regionIndex].comunas.length; j++) { //se recorre el archivo JSON por las comunas de la region seleccionada
                htmlComuna=htmlComuna+`<option value="${basedatos.regiones[regionIndex].comunas[j]}">${basedatos.regiones[regionIndex].comunas[j]}</option>`; //se suman las comunas al campo seleccionable comuna

            }
            document.getElementById("Comuna").innerHTML=htmlComuna; //se carga las comunas en el campo comuna
        }
    } catch (basedatos){}; //si hay un error en la lectura del archivo, se mostrara un mensaje de error de la funcion leerArchivo
}
async function MostrarRegion() {  //funcion que muestra las categorias, solo si no hay una categoria seleccionada
    try{
        if (ComprobarSelect()==false){ //si no hay datos de las regiones en el campo de regiones, se mostraran las regiones, si estan, no se mostraran mas datos
            
            const basedatos = await leerArchivo() //espera a que la funcion leerArchivo termine y guarde el archivo en la variable basedatos
            htmlRegion=`<option value="" selected="" disabled="">Escoja su Region</option>`; //se crea un placeholder sin valor
            htmlComuna=`<option value="" selected="" disabled="">Escoja su Comuna</option>`; //se crea un placeholder sin valor
            document.getElementById("Comuna").innerHTML=htmlComuna; //se muestra el placeholder en el campo comuna
            for (let i = 0; i < basedatos.regiones.length; i++) { //se recorre el archivo JSON por las regiones
                htmlRegion=htmlRegion+`<option value="${basedatos.regiones[i].region}">${basedatos.regiones[i].region}</option>`; //se muestra las regiones en el campo region una por una
                ArrayRegion.push(basedatos.regiones[i].region); //se guarda las regiones en un array definido fuera de la funcion para dps mostrar las comunas
            }
            document.getElementById("Region").innerHTML=htmlRegion;
        }
    }
    catch (basedatos){} //si hay un error en la funcion leerAchivo() se mostrara un mensaje de error
};
let ArrayRegion=[]; //declaro array para agregarle valores en mostrarregion y utilizarlo en mostrarcomuna
MostrarRegion(); //se ejecuta la funcion MostrarRegion al cargar la pagina

let regiones = document.getElementById('Region'); //selecciona el elemento con id categoria <select>

regiones.addEventListener('change', MostrarComuna); //agrega un event listener al elemento de id categoria que al cambiar ejecuta la funcion MostrarProducto <select>








