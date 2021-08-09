// Escribe un programa que contenga un método que acepte como parámetro una lista de números enteros mayores que 0, pudiendo contener elementos duplicados. Este método debe sustituir cada valor repetido por 0. Para terminar, realiza un método que muestre el array modificado. Nota: Necesitarás otro método para rellenar la lista de enteros. Le irá pidiendo números al usuario hasta que este introduzca un número negativo.

package semana_dos_ejercicios;

import java.util.*;

public class SustituirPorCeros {

    public static void solicitarNumeros(ArrayList <Integer> listaNumeros) {
        
        Integer numero;
        boolean contador = true;
        String salir = "Si";
        
        Scanner sc = new Scanner(System.in);
        System.out.println("------Lista de numeros Enteros----------");
        
        do {
            if (contador == true) {
                System.out.println("Introduce un numero mayor que 0 ");
                numero = sc.nextInt();
                if (numero <=0) {
                    System.out.println("El numero no es correcto!!!");
                }else{
                    listaNumeros.add(numero);
                    contador = false;
                }
            }

            System.out.println("Introduce otro numero: ");
            numero = sc.nextInt();
        
            if (numero <=0) {
                System.out.println("El numero no es correcto!!!");
            }else{
                listaNumeros.add(numero);
                contador = false;
            }
        
            System.out.println("Si quieres dejar de meter numeros escribe: \"Si\"");
            salir = sc.next();
        } while (salir.equalsIgnoreCase("No"));

        sc.close();
        //System.out.println(listaNumeros);
    }
    
    public static void rellenarDeCeros(ArrayList <Integer> listaNumeros) {
        ArrayList listaCopia = (ArrayList) listaNumeros.clone();
        for (int i = 0; i < listaNumeros.size(); i++) {
            for (int j = 0; j < listaCopia.size(); j++) {
                if ((i != j) && (listaNumeros.get(i) == listaCopia.get(j))) {
                    listaNumeros.set(i, 0);
                    listaNumeros.set(j, 0);
                }
            }
        }
        //System.out.println(listaNumeros);
    }

    public static void mostrarListas(ArrayList <Integer> listaNumeros) {
        System.out.println("------Lista de numeros Enteros----------");
        for (int i = 0; i < listaNumeros.size(); i++) {
            System.out.print(" " + listaNumeros.get(i) + " ");
        }
        System.out.println("");
    }

    public static void main(String[] args) {
        ArrayList <Integer> listaNumeros = new ArrayList <> ();
        solicitarNumeros(listaNumeros);
        mostrarListas(listaNumeros);
        rellenarDeCeros(listaNumeros);
        mostrarListas(listaNumeros);
    }
}