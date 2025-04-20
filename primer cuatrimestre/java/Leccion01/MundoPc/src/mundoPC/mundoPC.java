
package mundoPC;

import ar.com.system2023.mundopc.*;


public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP",13);//Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth","HP");
        Raton ratonHP = new Raton("Bluetooth","HP");
        Computadora computadoraHP = new Computadora("Computadora HP",monitorHP,tecladoHP,ratonHP);
        
        
        Monitor monitorGamer = new Monitor("HP",13);//Importar la clase
        Teclado tecladoGamer  = new Teclado("Bluetooth","Gamer ");
        Raton ratonGamer  = new Raton("Bluetooth","Gamer ");
        Computadora computadoraGamer  = new Computadora("Computadora Gamer ",monitorGamer ,tecladoGamer ,ratonGamer );
        Orden orden1 = new Orden();//Inicializamos el arreglo vacio
        Orden orden2 = new Orden();
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora computadoraVarias = new Computadora("Computadora de diferetnes marcas",monitorHP,tecladoGamer,ratonHP);
        orden2.agregarComputadora(computadoraVarias);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
    }
}
