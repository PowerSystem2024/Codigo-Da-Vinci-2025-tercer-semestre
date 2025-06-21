
package domain;


public class Rectangulo extends FiguraGeometrica {
    //Constructor
    
    public Rectangulo (String tipoFigura){
        super(tipoFigura);
    }
    
    @Override
    public void dibujar(){
        System.out.println("Se imprimo un: " + this.getClass().getSimpleName());
    }
    
}
