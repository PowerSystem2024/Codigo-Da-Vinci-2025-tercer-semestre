
const N = 8;  
let reinas = new Array(N).fill(0);

function valido(i) {
    /*  reina de la columna i
    no se amenaza con ninguna otra reina ya puesta */
    let v = true;
    for (let r = 0; r < i; r++) {
        v = v && (reinas[i] != reinas[r]); 
        v = v && (reinas[i] - i != reinas[r] - r); 
    }
    return v;
}

function mostrarTablero() {
    let tablero = new Array(N);
    for (let i = 0; i < N; i++) {
        tablero[i] = new Array(N).fill(0);
    }

    
    for (let i = 0; i < N; i++) {
        tablero[reinas[i]][i] = 1; 
    }

    console.log("\nMostrando arreglo de posiciones:");
    console.log(reinas.join("|"));

    console.log("\nMostrando el tablero:");
    for (let i = 0; i < N; i++) {
        let fila = "";
        for (let j = 0; j < N; j++) {
            fila += tablero[i][j] ? "Q " : ". ";
        }
        console.log(fila);
    }
}

function ponerReina(i, solucion) {
    let k = 0; // Inicializamos el conteo de movimientos
    solucion.valor = false;

    do {
        reinas[i] = k; 
        k++;

        if (valido(i)) { 
            if (i < N - 1) { 
                ponerReina(i + 1, solucion);
                
                
                if (!solucion.valor) {
                    reinas[i] = 0;
                }
            } else { 
                solucion.valor = true;
            }
        }
    } while (!solucion.valor && (k < N));
}


function resolverNReinas() {
    
    let solucion = { valor: false };
    
    ponerReina(0, solucion);

    if (solucion.valor) {
        console.log("Sí existe combinación de reinas");
        mostrarTablero();
    } else {
        console.log("No existe combinación de reinas");
    }
}


resolverNReinas();