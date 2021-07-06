package semana_dos_ejercicios;

import java.util.Calendar;

public class ProfesorInterino extends Profesor {
    
    private Calendar FechaComienzoInterinidad;
    
    //Constructor
    public ProfesorInterino(Calendar fechaComienzaInterinidad) {
    }

    //Constructor
    public ProfesorInterino (String nombre, String apellidos, int edad, Calendar fechaComienzaInterinidad) {
        super(nombre, apellidos, edad);
        FechaComienzoInterinidad = fechaComienzaInterinidad; 
    }

    //getter de la variable
    public Calendar getFechaComienzoInterinidad () { 
        return FechaComienzoInterinidad; 
    }

    //Polimorfismo en la forma de sobrescribir mostrarDatos de la clase "Profesor"
    public void mostrarDatos() { 
        System.out.println("Datos ProfesorInterino. Comienzo interinidad: " + FechaComienzoInterinidad.getTime().toString() );  
    }

}