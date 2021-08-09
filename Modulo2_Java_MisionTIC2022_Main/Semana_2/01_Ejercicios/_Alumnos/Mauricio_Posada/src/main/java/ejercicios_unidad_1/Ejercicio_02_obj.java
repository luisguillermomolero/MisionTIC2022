package ejercicios_unidad_1;

// Elaborado por Mauricio Posada Grupo P72
/*
2. Realizar un programa que realice el promedio de las notas de un alumno, para ello el programa va a tener
que solicitar el nombre del alumno y las notas de las 3 evaluaciones. Si el alumno tiene un promedio mayor o 
igual a 3.0 también debe imprimir “Aprobado”, si no alcanzó esa nota debe imprimir “Reprobado” . 
Requisitos: Las notas que se ingresan pueden tener decimales.
*/

import java.util.Scanner;

public class Ejercicio_02_obj {
    
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("\n-- Promedio de notas --\n");
        System.out.print("Introduce el nombre: ");
        String nombre = entrada.nextLine();

        Alumno alumno_01 = new Alumno(nombre);

        System.out.print("Introduce Nota 1: ");
        float nota1 = entrada.nextFloat();
        System.out.print("Introduce Nota 2: ");
        float nota2 = entrada.nextFloat();
        System.out.print("Introduce Nota 3: ");
        float nota3 = entrada.nextFloat();
        
        alumno_01.setNota_1(nota1);
        alumno_01.setNota_2(nota2);
        alumno_01.setNota_3(nota3);

        
        System.out.print(alumno_01.getResult());
        System.out.printf("%.2f", alumno_01.getPromedio());
        System.out.println();
        System.out.println();
        entrada.close();
        
    }

}
class Alumno {

    private String nombre;
    private float nota_01;
    private float nota_02;
    private float nota_03;
    private float promedio;

    public Alumno(String nombre){

        this.nombre = nombre;
    }

    public void setNota_1(float nota1) {
        this.nota_01 = nota1;
    }
    public void setNota_2(float nota2) {
        this.nota_02 = nota2;
    }
    public void setNota_3(float nota3) {
        this.nota_03 = nota3;
    }

    public float getNota1(){
        return this.nota_01;
    }

    public String getResult(){
        promedio = (nota_01 + nota_02 + nota_03) / 3;
        if (promedio >= 3) { // Construimos una condicional para verificar el estado final del alumno
			return "\nEl alumno " + nombre + " fue 'Aprobado' con un promedio de: ";
				
		} else {
			return "\nEl alumno " + nombre + " fue 'Reprobado' con un promedio de: ";
				
		}
    }

    public float getPromedio(){
        return promedio;
    }    
}