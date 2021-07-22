//Programa Java que lee el contenido del fichero creado en el Ejemplo 2 y lo muestra por pantalla.


package semana_cuatro_ejercicios;

import java.io.DataInputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class App {
    public static void main(String[] args) {
        FileInputStream fis = null;
        DataInputStream entrada = null;
        int filas, columnas, i, j;
        try {
            fis = new FileInputStream("matriz.dat"); //crea el archivo .dat
            entrada = new DataInputStream(fis);   // leer datos (primitivos)
            filas = entrada.readInt();            //se lee el primer entero del fichero                           
            columnas = entrada.readInt();         //se lee el segundo entero del fichero
            for (i = 0; i < filas; i++) {
                for (j = 0; j < columnas; j++) {  // se leen los double y se muestran por pantalla                
                    System.out.printf("%8.2f", entrada.readDouble());
                }
                System.out.println();
            }
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        } catch (EOFException e) {
            System.out.println("Fin de fichero");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if (fis != null) {
                    fis.close();
                }
                if (entrada != null) {
                    entrada.close();
                }
            } catch (IOException e) {
                System.out.println(e.getMessage());                                                               
            }
        }
    }
}