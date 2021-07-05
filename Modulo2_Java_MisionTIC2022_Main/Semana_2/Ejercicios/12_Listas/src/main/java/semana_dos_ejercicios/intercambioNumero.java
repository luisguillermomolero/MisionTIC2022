//Realizar un programa que lea tantos números enteros como desee el usuario y los introduzca en una lista. Muestras la lista, intercambia los números que se encuentren en la 2ª y 4ª posición, y muestras de nuevo la lista por consola. Utiliza al menos 3 métodos: uno para introducir los datos, otro para mostrar los datos y otro para intercambiar los datos

package semana_dos_ejercicios;

import java.util.*;

public class intercambioNumero {
    
    public static void introducirValores(ArrayList <Integer> listaNumeros){
        
        Scanner teclado = new Scanner(System.in);
        Integer numero;
        System.out.println("Introduce un numero: ");
        
        do {
            numero = teclado.nextInt();
            listaNumeros.add(numero);
            System.out.println("Introduce otro numero y si quieres salir introduce uno negativo");
        } while (numero >= 0);
        
        for (int i = 0; i < listaNumeros.size(); i++) {
            if (listaNumeros.get(i) < 0 ) {
                listaNumeros.remove(i);
            }
        }
        teclado.close();
    }
    
    public static void mostrarLista(ArrayList <Integer> listaNumeros){
        System.out.println("La lista contiene los siguientes números");
        System.out.println(listaNumeros);
    }
    
    public static void intercambiarPosiciones(ArrayList <Integer> listaNumeros){
        Integer aux;
        aux = listaNumeros.get(1);
        listaNumeros.set(1, listaNumeros.get(3));
        listaNumeros.set(3, aux);
    }

    public static void main(String[] args) {
        ArrayList <Integer> listaNumeros = new ArrayList <> ();
        introducirValores(listaNumeros);
        mostrarLista(listaNumeros);
        intercambiarPosiciones(listaNumeros);
        mostrarLista(listaNumeros);
    }
}