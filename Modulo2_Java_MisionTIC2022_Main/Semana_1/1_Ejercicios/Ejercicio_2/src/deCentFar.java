//Programa que lea un valor en grados centígrados y los convierte en grados Fahrenheit.La fórmula es: F = 32 + ( 9 * C / 5)

import java.util.*;

public class deCentFar {
  public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         double gradosC, gradosF;
         System.out.println("Por favor, introduzca los grados Centígrados:");
         gradosC = sc.nextDouble();
         
         //Calculo de grados F.
         gradosF = 32 + (9 * gradosC / 5);
         System.out.println(gradosC +" ºC = " + gradosF + " ºF ");
         sc.close();
  }
}