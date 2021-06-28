//Programa que lea un número entero y muestre si el número es múltiplo de 10

import java.util.Scanner;

public class Multiplo10 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N;
        System.out.print("Número entero: ");
        N = sc.nextInt();
        if(N%10==0)
           System.out.println("Es múltiplo de 10");   
        else
           System.out.println("No es múltiplo de 10");
    }
}