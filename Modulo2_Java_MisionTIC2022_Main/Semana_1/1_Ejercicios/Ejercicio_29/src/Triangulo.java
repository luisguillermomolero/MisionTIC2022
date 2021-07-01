//Programa lea la longitud de los catetos de un triángulo rectángulo y calcule la longitud de la hipotenusa según el teorema de Pitágoras.

import java.util.Scanner;

public class Triangulo {

    public static void main(String[] args) {

           Scanner sc = new Scanner(System.in);
           double cateto1, cateto2;

           System.out.print("Introduzca longitud del primer cateto: ");
           cateto1 = sc.nextDouble();

           System.out.print("Introduzca longitud del segundo cateto: ");
           cateto2 = sc.nextDouble();

           // raiz(cateto1² + cateto2²)         //Alt+253
           System.out.println("Hipotenusa -> " +  Math.sqrt(Math.pow(cateto1,2)+ Math.pow(cateto2, 2)));          
    }
}