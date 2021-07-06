package semana_dos_ejercicios;

import java.util.Calendar;

public class ProfesorTitular extends Profesor {
    
    private Calendar FechaComienzoSemestre;
    
    public ProfesorTitular(Calendar fechaComienzaSemestre) {
    }

    public ProfesorTitular (String nombre, String apellidos, int edad, Calendar fechaComienzaSemestre) {
        super(nombre, apellidos, edad);
        FechaComienzoSemestre = fechaComienzaSemestre; 
    }

    public Calendar getFechaComienzoInterinidad () { 
        return FechaComienzoSemestre; 
    }

    //Polimorfismo en la forma de sobrescribir mostrarDatos de la clase "Profesor"
    public void mostrarDatos() { 
        System.out.println("Datos ProfesorTitular. Comienzo Semestre: " + FechaComienzoSemestre.getTime().toString() );  
    }

}