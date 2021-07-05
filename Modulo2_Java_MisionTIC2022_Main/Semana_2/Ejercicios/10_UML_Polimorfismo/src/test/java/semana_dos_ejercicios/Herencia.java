package semana_dos_ejercicios;

import java.util.Calendar;

public class Herencia {

    public static void main (String [ ] Args) {
        
        Profesor profesor1 = new Profesor ("Juan", "Hernández García", 33);
        profesor1.setIdProfesor("Prof 22-387-11");

        Profesor profesor2 = new Profesor ("Carlos", "Rincon Mendez", 28);
        profesor2.setIdProfesor("Prof 58-111-29");

        Calendar fecha1 = Calendar.getInstance();
        Calendar fecha2 = Calendar.getInstance();

        fecha1.set(2021,06,01); //Los meses van de 0 a 11, luego 10 representa noviembre
        fecha2.set(2021,06,12); //Los meses van de 0 a 11, luego 10 representa noviembre

        ProfesorTitular titular1 = new ProfesorTitular("Luis Guillermo", "Molero Belloso", 40, fecha1);
        
        ProfesorInterino interino1 = new ProfesorInterino("José Luis", "Morales Pérez", 54, fecha2);
        
        ListinProfesores listin1 = new ListinProfesores ();

        listin1.addProfesor(profesor1);
        listin1.addProfesor(profesor2);
        listin1.addProfesor(titular1);
        listin1.addProfesor(interino1);
        listin1.listar();
        System.out.println();
    }
}