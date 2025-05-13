'use strict';
// usamos el bloque try-catch para evitar errores
try{
   let x= 152;  // lo traemos con alt + flecha hacia arriba o abajo
    mifuncion(); //capturamos el error de la funcion porque estaba x=10 pero no tenia el let
    throw'mi error'; //maneja tipo string
}
catch(error){ // catchamos el error
    console.log(typeof(error));
}
finally{
    console.log('termina la revision de errores');
}
//la ejecucion ahora continua

let resultado = '';
try {
    y = 8;
    if(isNaN(resultado)) throw 'no es un numero';
    else if(resultado === '') throw'es cadena vacia';
    else if(resultado >= 0) throw'valor positivo';
    else if(resultado <= 0) throw'valor negativo';
} 
catch (error) {
    
    console.log(error);
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally{
    console.log('termina la revision 2');
}