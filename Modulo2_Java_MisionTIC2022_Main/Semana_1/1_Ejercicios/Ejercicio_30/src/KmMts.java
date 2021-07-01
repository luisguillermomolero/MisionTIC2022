//Programa que pase una velocidad en Km/h a Mts/s. La velocidad se lee por teclado.

//import java.util.Scanner;

public class KmMts {

  public static void main(String[] args) {

        //  Scanner sc = new Scanner(System.in);
         double velocidad = 55;
        //  System.out.println("Introduzca velocidad en Km/h: ");
        //  velocidad = sc.nextDouble();
         System.out.println(velocidad + " Km/h -> " + velocidad*1000/3600 + " m/s");                              
  }
}