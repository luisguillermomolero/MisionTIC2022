//Programa que pase una velocidad en Km/h a m/s. La velocidad se lee por teclado.

import java.util.Scanner;

public class KmaMts {

  public static void main(String[] args) 
  {

         Scanner sc = new Scanner(System.in);
         double velocidad;
         System.out.println("Introduzca velocidad en Km/h: ");
         velocidad = sc.nextDouble();
         System.out.println(velocidad + " Km/h -> " + velocidad*1000/3600 + " m/s");                              
  }
}