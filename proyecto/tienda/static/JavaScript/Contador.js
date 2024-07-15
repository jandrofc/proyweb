const getRemainTime = deadline => {//Función que recibe la fecha límite
  let now = new Date(),//Fecha actual
      remainTime = (new Date(deadline) - now + 1000) / 1000,//Tiempo restante para fecha limite se divide entre 1000 para obtener segundos ya que esta en milisegundos y en segundos facilita mas la operacion
      remainSeconds = ('0' + Math.floor(remainTime % 60)).slice(-2),//Se obtienen los segundos restantes (Se agrega 0 al inicio y se toman los últimos 2 dígitos para que siempre sean 2 dígitos)
      remainMinutes = ('0' + Math.floor(remainTime / 60 % 60)).slice(-2),//Se obtienen los minutos restantes (60 segundos en un minuto)
      remainHours = ('0' + Math.floor(remainTime / 3600 % 24)).slice(-2),//Se obtienen las horas restantes (3600 segundos en una hora y 24 horas en un día)
      remainDays = Math.floor(remainTime / (3600 * 24));//Se obtienen los días restantes (3600 segundos en una hora y 24 horas en un día)

  return {
    remainTime,
    remainSeconds,
    remainMinutes,
    remainHours,
    remainDays
  }
}

const countdown = (deadline) => {//Función que recibe la fecha límite, el elemento donde se mostrará el contador y el mensaje final
    const elDays = document.getElementById('dias');
    const elHours = document.getElementById('horas');
    const elMinutes = document.getElementById('minutos');
    const elSeconds = document.getElementById('segundos');
    let timerUpdate;//Variable para almacenar el intervalo
    const updateCountdown = () => {//Función que actualiza el contador
        let t = getRemainTime(deadline);//Se obtiene el tiempo restante
        console.log(t);
        elDays.innerHTML = ` ${t.remainDays}`;//Se muestra el tiempo restante en el elemento
        elHours.innerHTML = ` ${t.remainHours}`;
        elMinutes.innerHTML = ` ${t.remainMinutes}`;
        elSeconds.innerHTML = ` ${t.remainSeconds}`;
      if(t.remainTime <= 0) {//Si el tiempo restante es menor o igual a 0
        clearInterval(timerUpdate);//Se detiene el intervalo
        let sorteoDiv = document.getElementById('oferta');//Se obtiene el elemento donde se mostrará el sorteo
        sorteoDiv.style.display = 'none';//Se oculta el sorteo
      }
    }
    updateCountdown(); // Llama a la función de actualización una vez antes de iniciar el intervalo

    timerUpdate = setInterval(updateCountdown, 1000);
}

countdown('2024-07-28T23:59:59','America/Santiago');//Se llama a la función countdown con la fecha límite, el elemento donde se mostrará el contador y el mensaje final