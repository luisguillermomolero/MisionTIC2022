package semana_dos_ejercicios;

public class Persona {
    private String nombre;
    private int edad;

    public Persona(){
    }

    public int getEdad(){
        return edad;
    }

    public void setEdad(int val){
        this.edad = val;
    }

    public String getNombre(){
        return nombre;
    }

    public void setNombre(String val){
        this.nombre = val;
    }
}
