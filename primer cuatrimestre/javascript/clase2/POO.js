/*
2.2 Repasamo la sobreescritura ahora en JavaScript

avanzamos hacia el polimorfismo.
la sobreescritura tiene que ver con la herencia de pafdrea a hijo, la clase hija hereda de la clase padre
pero agrega su `propio comportamiento.
creamos la clase empleado (padre)
trabajamos con encaps para el nombre y sueldo
creamos el metodo obtener detalles
retornaraà: nombre , con el template string  y sueldo
*/

class Empleado {
    constructor(nombre,sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }
    obtenerDetalles(){
        return `Empleado: nombre: ${this._nombre}, sueldo: ${this._sueldo}`;
    }
}
class Gerente extends Empleado{
    constructor(nombre,sueldo,departamento){
        super(nombre,sueldo);
        this._departamento = departamento;
    }
    // agregamos la sobreescritura
    obtenerDetalles(){ // metodo donde se puede apreciar la sobreescritura
        return `Gerente: ${super.obtenerDetalles()} depto: ${this._departamento}`;
    }
}

let gerente1 = new Gerente("Carlos",5000,"Sistemas"); //muestra todo del gerente
console.log(gerente1); // objeto de la clase hija

let empleado1 = new Empleado("Juan ",3000,"Administracion"); // muestra todo del empleado
console.log(empleado1); // objeto de la clase padre