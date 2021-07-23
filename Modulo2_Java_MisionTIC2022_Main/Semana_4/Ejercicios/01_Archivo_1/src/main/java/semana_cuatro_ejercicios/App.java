package semana_cuatro_ejercicios;

import java.io.*;

public class App {
public static void main(String args[]) {
    int numBytes = 0;
    char caracter;
    System.out.println("\nEscribe el texto: ");
    try {
        do {
            caracter = (char)System.in.read();
            System.out.print(caracter);
            numBytes++;
        } while (caracter != '\n');
        System.out.printf("%d bytes leidos %n", numBytes);
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}