
package domain;


public class Persona {
    private final int idPersona;
    private static int contadorPersona;
    
    static{
        System.out.println("Ejecucion del bloque estatico ");
        ++Persona.contadorPersona;
        //idPersona=10; No es estatico por esto tenemos error
    }
    
    {//Bloque de inicializacion NO  estatico(contecto dinamico)
        System.out.println("Ejecucion del bloque No estatico");
        this.idPersona = Persona.contadorPersona++;//Incrementamos el atributo        
        
    }
    
    //Los bloques de inicializacion se ejecutan antes del contructor
    public Persona(){
        System.out.println("Ejecucion del constuctor");
    }
    public int idPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
