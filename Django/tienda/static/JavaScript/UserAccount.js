function AbrirCuenta(){
    var cuenta = document.getElementById("pop-up");
    if (cuenta.style.display === "none" || cuenta.style.display === "") {
        cuenta.style.display = "flex";
    } else {
        cuenta.style.display = "none";
    }
}

