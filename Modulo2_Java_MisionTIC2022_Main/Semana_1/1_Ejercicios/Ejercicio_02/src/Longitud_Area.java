// Programa que lee por teclado el valor del radio de una circunferencia y calcula y muestra por pantalla la longitud y el área de la circunferencia.

import java.util.*;

public class Longitud_Area {

    public static void main(String[] args) {

           Scanner sc = new Scanner(System.in);
           double radio, longitud, area, area2;
           System.out.println("Introduce radio de la circunferencia:");
           radio = sc.nextDouble();
           longitud = 2 * Math.PI * radio;
           area = Math.PI * Math.pow(radio, 2);
           area2 = 3.14*(radio*radio);
           System.out.println("La longitud de la circunferencia -> " + longitud);                                     
           System.out.println("Área de la circunferencia -> " + area);
           System.out.println("El área de la circunferencia 2 -> " + area2);
    }
}