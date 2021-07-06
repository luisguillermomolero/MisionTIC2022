package semana_dos_ejercicios;

import java.util.Calendar;

public class ProfesorInterino extends Profesor {
    
    private Calendar FechaComienzoInterinidad;
    
    public ProfesorInterino(Calendar fechaComienzaInterinidad) {
    }

    public ProfesorInterino (String nombre, String apellidos, int edad, Calendar fechaComienzaInterinidad) {
        super(nombre, apellidos, edad);
        FechaComienzoInterinidad = fechaComienzaInterinidad; 
    }

    public Calendar getFechaComienzoInterinidad () { 
        return FechaComienzoInterinidad; 
    }

    //Polimorfismo en la forma de sobrescribir mostrarDatos de la clase "Profesor"
    public void mostrarDatos() { 
        System.out.println("Datos ProfesorInterino. Comienzo interinidad: " + FechaComienzoInterinidad.getTime().toString() );  
    }

}