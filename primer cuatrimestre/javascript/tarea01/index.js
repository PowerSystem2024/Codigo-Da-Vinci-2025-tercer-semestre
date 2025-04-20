// Clase base
class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
      this._tipoEntrada = tipoEntrada;
      this._marca = marca;
    }
  
    get tipoEntrada() {
      return this._tipoEntrada;
    }
  
    set tipoEntrada(valor) {
      this._tipoEntrada = valor;
    }
  
    get marca() {
      return this._marca;
    }
  
    set marca(valor) {
      this._marca = valor;
    }
  
    toString() {
      return `Tipo de entrada: ${this._tipoEntrada}, Marca: ${this._marca}`;
    }
  }
  
  // RATÓN
  class Raton extends DispositivoEntrada {
    static contadorRatones = 0;
  
    constructor(tipoEntrada, marca) {
      super(tipoEntrada, marca);
      this._idRaton = ++Raton.contadorRatones;
    }
  
    get idRaton() {
      return this._idRaton;
    }
  
    toString() {
      return `Ratón [ID: ${this._idRaton}] - ${super.toString()}`;
    }
  }
  
  // TECLADO
  class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0;
  
    constructor(tipoEntrada, marca) {
      super(tipoEntrada, marca);
      this._idTeclado = ++Teclado.contadorTeclados;
    }
  
    get idTeclado() {
      return this._idTeclado;
    }
  
    toString() {
      return `Teclado [ID: ${this._idTeclado}] - ${super.toString()}`;
    }
  }
  
  // MONITOR
  class Monitor {
    static contadorMonitores = 0;
  
    constructor(marca, tamanio) {
      this._idMonitor = ++Monitor.contadorMonitores;
      this._marca = marca;
      this._tamanio = tamanio;
    }
  
    get idMonitor() {
      return this._idMonitor;
    }
  
    get marca() {
      return this._marca;
    }
  
    set marca(valor) {
      this._marca = valor;
    }
  
    get tamanio() {
      return this._tamanio;
    }
  
    set tamanio(valor) {
      this._tamanio = valor;
    }
  
    toString() {
      return `Monitor [ID: ${this._idMonitor}] - Marca: ${this._marca}, Tamaño: ${this._tamanio}"`;
    }
  }
  
  // COMPUTADORA
  class Computadora {
    static contadorComputadoras = 0;
  
    constructor(nombre, monitor, teclado, raton) {
      this._idComputadora = ++Computadora.contadorComputadoras;
      this._nombre = nombre;
      this._monitor = monitor;
      this._teclado = teclado;
      this._raton = raton;
    }
  
    get idComputadora() {
      return this._idComputadora;
    }
  
    get nombre() {
      return this._nombre;
    }
  
    set nombre(valor) {
      this._nombre = valor;
    }
  
    get monitor() {
      return this._monitor;
    }
  
    set monitor(valor) {
      this._monitor = valor;
    }
  
    get teclado() {
      return this._teclado;
    }
  
    set teclado(valor) {
      this._teclado = valor;
    }
  
    get raton() {
      return this._raton;
    }
  
    set raton(valor) {
      this._raton = valor;
    }
  
    toString() {
      return `Computadora [ID: ${this._idComputadora}, Nombre: ${this._nombre}]\n  ${this._monitor}\n  ${this._teclado}\n  ${this._raton}`;
    }
  }
  
  // ORDEN
  class Orden {
    static contadorOrdenes = 0;
  
    constructor() {
      this._idOrden = ++Orden.contadorOrdenes;
      this._computadoras = [];
    }
  
    get idOrden() {
      return this._idOrden;
    }
  
    get computadoras() {
      return this._computadoras;
    }
  
    agregarComputadora(computadora) {
      this._computadoras.push(computadora);
    }
  
    mostrarOrden() {
      let resultado = `Orden [ID: ${this._idOrden}]\n`;
      this._computadoras.forEach((compu, i) => {
        resultado += `  Computadora ${i + 1}:\n${compu.toString()}\n`;
      });
      return resultado;
    }
  
    toString() {
      return this.mostrarOrden();
    }
  }
  
  // 🔽 PRUEBAS
  const monitor1 = new Monitor("Samsung", 27);
  const teclado1 = new Teclado("USB", "Logitech");
  const raton1 = new Raton("Bluetooth", "Razer");
  const compu1 = new Computadora("Gamer", monitor1, teclado1, raton1);
  
  const monitor2 = new Monitor("LG", 24);
  const teclado2 = new Teclado("USB", "Genius");
  const raton2 = new Raton("USB", "HP");
  const compu2 = new Computadora("Oficina", monitor2, teclado2, raton2);
  
  const orden1 = new Orden();
  orden1.agregarComputadora(compu1);
  orden1.agregarComputadora(compu2);
  
  console.log(orden1.toString());
  