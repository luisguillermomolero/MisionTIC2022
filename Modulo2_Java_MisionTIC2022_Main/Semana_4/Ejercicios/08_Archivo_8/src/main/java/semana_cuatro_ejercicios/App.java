package semana_cuatro_ejercicios;

import java.io.File;  // Importar la clase de archivo
import java.io.IOException;  // Importar la clase IOException para manejar errores

public class App {
  public static void main(String[] args) {
    try {
      File myObj = new File("filename.txt");
      if (myObj.createNewFile()) {
        System.out.println("Archivo creado: " + myObj.getName());
      } else {
        System.out.println("El archivo ya existe.");
      }
    } catch (IOException e) {
      System.out.println("Ocurrio un ERROR.");
      e.printStackTrace();
    }
  }
}