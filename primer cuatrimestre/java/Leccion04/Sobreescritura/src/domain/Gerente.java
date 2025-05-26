package domain;

public class Gerente extends Empleado {
    private String departamento;

    public Gerente(String nombre, Double sueldo, String departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }
    //Sobreescribimos el método
    @Override
    public String obtenerDetalles() {
        return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }
}
