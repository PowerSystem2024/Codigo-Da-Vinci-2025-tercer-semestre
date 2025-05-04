'use strict';

// Primer bloque try-catch-finally
try {
    let x = 10;
    mifuncion(); // Esta función no está definida, lanza error

    /* function mifuncion() {
    console.log("Hola desde mifuncion");
}

let x = 10;
mifuncion();  // Ahora sí está definida*/


    throw 'mi error'; // Esto también lanzará un error si llegara a esta línea
} catch (error) {
    console.log(typeof(error)); // <-- estaba escrito como 'etypeof'
    console.log('Error capturado:', error);
} finally {
    console.log('Termina la revisión de errores (bloque 1)');
}

// Segundo bloque, probando diferentes valores para resultado
let valoresDePrueba = [NaN, '', 5, -3];

for (let i = 0; i < valoresDePrueba.length; i++) {
    let resultado = valoresDePrueba[i];
    console.log('\nProbando con resultado =', resultado);

    try {
        if (isNaN(resultado)) throw new Error('No es un número');
        else if (resultado === '') throw new Error('Es cadena vacía');
        else if (resultado >= 0) throw new Error('Valor positivo');
        else if (resultado <= 0) throw new Error('Valor negativo');
    } catch (error) {
        console.log('Error capturado:', error.message);
        console.log('Nombre del error:', error.name);
    } finally {
        console.log('Termina la revisión (bloque 2)');
    }
}