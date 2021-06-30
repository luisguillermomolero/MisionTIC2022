// Programa que lea dos números por teclado y muestre el resultado de su división. Se comprueba que el divisor sea distinto de cero.

import java.util.Scanner;

public class Division {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double dividendo, divisor;

        System.out.print("Por favor, introduzca el dividendo: ");
        dividendo = sc.nextDouble();
        System.out.print("Por favor, Introduzca el divisor: ");
        divisor = sc.nextDouble();

        if(divisor==0){
           System.out.println("No se puede dividir por cero");   
        }else{
            System.out.println(dividendo + " / " + divisor + " = " + dividendo/divisor);
            //System.out.printf("%.2f / %.2f = %.2f %n" , dividendo, divisor , dividendo/divisor);
        }
    sc.close();
    }
}