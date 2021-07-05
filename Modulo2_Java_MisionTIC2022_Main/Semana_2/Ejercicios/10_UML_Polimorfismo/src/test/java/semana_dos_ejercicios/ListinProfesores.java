package semana_dos_ejercicios;

import java.util.ArrayList;

public class ListinProfesores{

    private ArrayList <Profesor> listinProfesores;

    public ListinProfesores () {
        listinProfesores = new ArrayList <Profesor> (); 
    }

    public void addProfesor (Profesor profesor) {
        listinProfesores.add(profesor); 
    }

    public void listar() {
        System.out.println ("\nSe procede a mostrar los datos de los profesores existentes en el listín \n");
        for (Profesor tmp: listinProfesores) {       //Uso de for extendido
            tmp.mostrarDatos(); }
    }
}