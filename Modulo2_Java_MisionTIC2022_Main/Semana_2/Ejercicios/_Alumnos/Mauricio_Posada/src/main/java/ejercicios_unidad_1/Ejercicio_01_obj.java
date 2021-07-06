package ejercicios_unidad_1;

//Elaborado por Mauricio Posada

/* 1. Realizar la suma, la resta, la división y la multiplicación de dos números leídos por teclado y mostrar 
* en pantalla “La <operación> de <número 1> y <número 2> es igual a <resultado> ”. */

import java.util.Scanner;

public class Ejercicio_01_obj {

    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);

        System.out.print("\n-- Operaciones aritméticas\n");
        System.out.print("Introduce Numero 1: ");
        float num_1 = entrada.nextFloat();
        
        System.out.print("Introduce Numero 2: ");
        float num_2 = entrada.nextFloat();
        
        
        Operaciones ejercicio = new Operaciones(num_1, num_2); // Instanciar un objeto

        System.out.println("La suma de " + ejercicio.getNum_1() + " y " + ejercicio.getNum_2() + " es igual a " + ejercicio.getSuma());
        System.out.println("La resta de " + ejercicio.getNum_1() + " menos " + ejercicio.getNum_2() + " es igual a " + ejercicio.getResta());
        System.out.println("La multiplicacion de " + ejercicio.getNum_1() + " x " + ejercicio.getNum_2() + " es igual a " + ejercicio.getMultiplicacion());
        System.out.println("La division de " + ejercicio.getNum_1() + " entre " + ejercicio.getNum_2() + " es igual a " + ejercicio.getDivision());
        
        entrada.close();
    }
    
}

class Operaciones {

    private float num_1;
    private float num_2;
    
    public Operaciones (float num_1, float num_2){ // Constructor
        this.num_1 = num_1;
        this.num_2 = num_2;
    }

    public float getSuma(){
        return num_1 + num_2;
    }

    public float getResta(){
        return num_1 - num_2;
    }

    public float getMultiplicacion(){
        return num_1 * num_2;
    }

    public float getDivision(){
        return num_1 / num_2;
    }


    public float getNum_1(){
        return this.num_1;
    }

    public float getNum_2(){
        return this.num_2;
    }

    

}




