/*
function MostrarCaja(e){
    //e.preventDefault();
    var id = e.currentTarget.id;  // Obtiene el id de la caja que se ha clickeado, la id la tiene el evento es deir e
    var detalle;

    switch(id){
        case "caja1":
            detalle = document.getElementById("detalle1"); 

            if (detalle.style.visibility === null || detalle.style.visibility === "" || detalle.style.visibility === "hidden") {
                detalle.style.visibility = "visible";
            }
            else {
                detalle.style.visibility = "hidden";
            }
            break;
        case "caja2":
            detalle = document.getElementById("detalle2");
        
            if (detalle.style.visibility === "" || detalle.style.visibility === "hidden") {
            detalle.style.visibility = "visible";
            }
            else {
            detalle.style.visibility = "hidden";
            }
            break;
        case "caja3":
            detalle = document.getElementById("detalle3");
        
            if (detalle.style.visibility === "" || detalle.style.visibility === "hidden") {
            detalle.style.visibility = "visible";
            }
            else {
            detalle.style.visibility = "hidden";
            }
            break;
        case "caja4":
            detalle = document.getElementById("detalle4");
        
            if (detalle.style.visibility === "" || detalle.style.visibility === "hidden") {
            detalle.style.visibility = "visible";
            }
            else {
            detalle.style.visibility = "hidden";
            }
            break;
        case "caja5":
            detalle = document.getElementById("detalle5");
        
            if (detalle.style.visibility === "" || detalle.style.visibility === "hidden") {
            detalle.style.visibility = "visible";
            }
            else {
            detalle.style.visibility = "hidden";
            }
            break;
        case "caja6":
            detalle = document.getElementById("detalle6");
        
            if (detalle.style.visibility === "" || detalle.style.visibility === "hidden") {
            detalle.style.visibility = "visible";
            }
            else {
            detalle.style.visibility = "hidden";
            }
            break;
        default:
            // Default code if id doesn't match any case
            console.log("ERROR: ID no encontrado en el switch de MostrarCaja()");
    }
}


*/