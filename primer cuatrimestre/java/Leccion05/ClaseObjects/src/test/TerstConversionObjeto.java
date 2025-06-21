
package test;

import Domain.*;


public class TerstConversionObjeto {
    public static void main(String[] args){
        Empleado empleado1 = new Empleado("juan",5000);
        Empleado empleado2 = new Empleado("Juan",5000);
        
        if(empleado1== empleado2){
            System.out.println("Tine la misma referencia en memoria");
        }
        else{
            System.out.println("Tine distinta referencia en memoria ");
        }
        
        if(empleado1.equals(empleado2)){
            System.out.println("Los objetos son iguales en contenido ");
        }
        else{
            System.out.println("Los objetos son distintos en contenido ");       
        }
       
       
    }
    
}
