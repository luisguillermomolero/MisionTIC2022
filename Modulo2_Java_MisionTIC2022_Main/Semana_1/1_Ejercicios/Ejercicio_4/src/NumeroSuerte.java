//Programa que pida por teclado la fecha de nacimiento de una persona (dia, mes, año) y calcule su número de la suerte. Este número, se calcula sumando el día, mes y año de la fecha de nacimiento y a continuación, sumando las cifras obtenidas en la suma.

import java.util.Scanner;

public class NumeroSuerte {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dia, mes, año, suerte, suma, cifra1, cifra2, cifra3, cifra4;

        System.out.println("Por favor, introduzca su fecha de nacimiento");
        System.out.print("día: ");
        dia = sc.nextInt();
        
        System.out.print("mes: ");
        mes = sc.nextInt();
        
        System.out.print("año: ");
        año = sc.nextInt();
        
        suma = dia + mes + año;
        
        cifra1 = suma/1000;      //obtiene la primera cifra
        cifra2 = suma/100%10;    //obtiene la segunda cifra
        cifra3 = suma/10%10;     //obtiene la tercera cifra
        cifra4 = suma%10;        //obtiene la última cifra
        suerte = cifra1 + cifra2 + cifra3 + cifra4;
        System.out.println("Su número de la suerte es: " + suerte);
        sc.close();
    }
}