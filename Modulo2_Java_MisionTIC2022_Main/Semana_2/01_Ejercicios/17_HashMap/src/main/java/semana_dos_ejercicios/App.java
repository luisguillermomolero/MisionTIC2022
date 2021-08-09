// Declaración de un Map (un HashMap) con clave "Integer" y Valor "String". Las claves pueden ser de cualquier tipo de objetos, aunque los más utilizados como clave son los objetos predefinidos de Java como String, Integer, Double ... !!!!CUIDADO los Map no permiten datos atómicos

package semana_dos_ejercicios;

import java.util.*;

public class App {
    public static void main(String[] args) {
  
      HashMap<Integer, String> m = new HashMap<>();
  
      m.put(924, "Amalia Núñez");
      m.put(921, "Cindy Nero");
      m.put(700, "César Vázquez");
      m.put(219, "Víctor Tilla");
      m.put(537, "Alan Brito");
      m.put(605, "Esteban Quito ");
  
      System.out.println("Todas las entradas del diccionario extraídas con entrySet:");
      System.out.println(m.entrySet());
  
      System.out.println("\nEntradas del diccionario extraídas una a una:");
      for (Map.Entry pareja: m.entrySet()) {
        System.out.println(pareja);
      }    
    }
  }