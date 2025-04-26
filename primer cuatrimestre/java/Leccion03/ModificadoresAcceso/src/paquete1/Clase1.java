
package paquete1;

public class Clase1 {
    public String atributoPublic = "Valor atributo Public" ;
    protected String atributoProtected ="valor atributo protected";
   
    public Clase1(){
        System.out.println("Constructor publico");
    }
    
    protected Clase1(String atributoPublic){
        System.out.println("Constructor protected");
    }
    
    public void metodoPublico(){
        System.out.println("Metodo Public");
    }
    
    protected void metodoPortected(){
        System.out.println("Metodo protected");
    }
}
