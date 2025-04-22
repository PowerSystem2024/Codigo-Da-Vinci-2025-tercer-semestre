/*

2.2 Creamos un archivo de la clase de hoy y le ponemos de nombre: 02-ModoStrict.js

Debido a las diferentes actualizaciones, en el día de hoy hay cosas que han 
ido cambiando, hoy vamos a ver hasta donde es que se puede utilizar este modo strict:
  Vamos a usar el concepto de , para evitar la practica de usar variables sin de
  clarar.
  Generamos una cadena use strict, estamos agregando el modo estrcito a nuestro
  programa.Generamos una variable  x=10 y con el console lo imprimimos.
*/

"use strict";

// x= 10; // x no esta definida
const x = 10; // aqui ya esta definida
console.log(x);

miFuncion();

function miFuncion(){
    //"use strict";si lo comentamos , sigue funcionando
    y = 10;
    console.log(y);
}
miFuncion();



