function AbrirCuenta(){
    var cuenta = document.getElementById("pop-up");
    if (cuenta.style.display === "none" || cuenta.style.display === "") {
        cuenta.style.display = "flex";
    } else {
        cuenta.style.display = "none";
    }
}

function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
  }
  

