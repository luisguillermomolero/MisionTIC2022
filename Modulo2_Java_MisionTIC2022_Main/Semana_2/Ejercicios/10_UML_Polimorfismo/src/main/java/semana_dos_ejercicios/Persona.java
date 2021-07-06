package semana_dos_ejercicios;

public class Persona {

    private String nombre; 
    private String apellidos; 
    private int edad;

    //Constructor
    public Persona() { 
    }

    //Constructor
    public Persona (String nombre, String apellidos, int edad) {
        this.nombre = nombre; 
        this.apellidos = apellidos; 
        this.edad = edad; 
    }

    //getter de variables
    public String getNombre() { 
        return nombre;  
    }

    public String getApellidos () { 
        return apellidos;  
    }

    public int getEdad() { 
        return edad;  
    }
}