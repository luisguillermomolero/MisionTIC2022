//Desarrolle un programa que elimine las cadenas duplicadas de un objeto "List". 
//Hacer uso del objeto HashSet.


package semana_dos_ejercicios;

import java.util.List;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.Collection;

public class PruebaSet {
    
    private String colores[] = {"rojo", "blanco", "azul", "verde", "gris", "naranja", "carne", "blanco", "cyan", "gris", " naranja "};
    
    public PruebaSet() {
        List<String> lista = Arrays.asList(colores);
        System.out.printf("ArrayList: %s \n", lista);
        imprimirSinDuplicados(lista);
    }

    private void imprimirSinDuplicados(Collection<String> coleccion) {
        Set<String> conjunto = new HashSet<String>(coleccion);
        System.out.println("\nLos valores sin duplicados son: ");
        
        for (String string : conjunto) {
            System.out.println(string);
        }
    }

    public static void main(String args[]) {
        new PruebaSet();
    }
}