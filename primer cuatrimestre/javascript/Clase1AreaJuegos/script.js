// poner aqui la funcion
// necesitamos que de manera random use nros aleatorios usando el metodo random, math.floor(quita los decimales
// min = 1 max=3
// hacer una funcion con esa formula random donde yo la llame a la funcion con parametros y argumentos, para que trabaje aleatoriamente,
// para que la variable pc tenga nros aleatorios
// 1 será piedra, 2 será papel, 3 será tijera

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let min = 1;
let max = 3;

function play(jugador) {
    let pc = getRandomInt(min, max);

    let elecciones = ["", "🪨 Piedra", "📄 Papel", "✂️ Tijera"];
    let mensaje = "Elegiste: " + elecciones[jugador] + "<br>";
    mensaje += "La computadora eligió: " + elecciones[pc] + "<br>";

    if (jugador === pc) {
        mensaje += "<strong>¡Empate!</strong>";
    } else if (
        (jugador === 1 && pc === 3) ||
        (jugador === 2 && pc === 1) ||
        (jugador === 3 && pc === 2)
    ) {
        mensaje += "<strong>¡Ganaste!</strong>";
    } else {
        mensaje += "<strong>Perdiste</strong>";
    }

    document.getElementById("resultado").innerHTML = mensaje;

    // desactiva los botones hasta que reinicie
    document.querySelectorAll(".buttons button").forEach(btn => {
        btn.disabled = true;
    });
}

// Botón para reiniciar el juego
function reiniciarJuego() {
    document.getElementById("resultado").innerHTML = "";
    document.querySelectorAll(".buttons button").forEach(btn => {
        btn.disabled = false;
    });
}