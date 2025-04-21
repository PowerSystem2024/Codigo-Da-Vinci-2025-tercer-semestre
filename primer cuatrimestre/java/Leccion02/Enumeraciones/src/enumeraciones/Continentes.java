
package enumeraciones;


public enum Continentes {
    AFRICA(54 , "1.2 billones"),
    EUROPA(46, "2 billones"),
    ASIA(44, "1 billones"),
    AMERICA(34, "3 billones"),
    OSEANIA(14, "1 billones");
    
  private final int paises;
  private String habitantes;
  
  Continentes(int paises, String habitantes){
      this.paises = paises;
      this.habitantes = habitantes;
  }
  
  //Metodo Get
  public int getPaises(){
      return this.paises;
  }
  
  public String getHabitantes(){
      return this.habitantes;
  }
}
