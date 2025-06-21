function torresHanoi(n, origen = 'A', auxiliar = 'B', destino = 'C') {
    if (n === 1) {
        console.log(`Mover disco 1 de ${origen} a ${destino}`);
        return;
    }
    
    torresHanoi(n - 1, origen, destino, auxiliar);
    console.log(`Mover disco ${n} de ${origen} a ${destino}`);
    torresHanoi(n - 1, auxiliar, origen, destino);
}

console.time("Tiempo de ejecución");
torresHanoi(8);
console.timeEnd("Tiempo de ejecución");