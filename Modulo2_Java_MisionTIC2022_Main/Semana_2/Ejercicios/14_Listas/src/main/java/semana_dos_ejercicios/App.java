package semana_dos_ejercicios;

import java.util.*;

public class App {
    
    
    public static void main(String[] args) {
        
        ArrayList <Integer> listaEnteros = new ArrayList<>();
        //var listaEnteros = new ArrayList<Integer>();
        listaEnteros.add(4);
        listaEnteros.add(5);
        listaEnteros.add(7);
        listaEnteros.add(2, 6); // Agrega 6 entre 5 y 7

        System.out.println("El tamaño de la lista es de :"+ listaEnteros.size()+"\n"); // 4);

        Scanner sc = new Scanner (System.in);
        System.out.println("Introduzca el número a buscar? ");
        int buscar = sc.nextInt();

        for (int i=0;i<=listaEnteros.size(); i++){
            if (listaEnteros.contains(buscar) == true){
                System.out.println("Si esta");
                break;
            }else{
                System.out.println("No esta");
                break;
            }
        }

        System.out.println("Introduce un número y te devuelvo su posición: ");
        int buscar2 = sc.nextInt();

        for (int m=0;m<=listaEnteros.size();m++){
            if (listaEnteros.contains(buscar2) == true){
                System.out.println("Esta en la posición: "+listaEnteros.indexOf(buscar2));
                break;
            }else{
                System.out.println("No esta");
                break;
            }
        }
        sc.close();
    }
}
