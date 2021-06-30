import java.util.Scanner;

public class sumaNumeros {

    public static void main(String[] args){

        //declaración de variables
        int n1, n2;
        Scanner sc = new Scanner(System.in);

        //leer el primer número
        System.out.println("Por favor, introduzca un número entero: ");
        n1 = sc.nextInt();      //lee un entero por teclado

        //leer el segundo número
        System.out.println("Por favor, introduzca un segundo número: ");
        n2 = sc.nextInt();      //lee un entero por teclado
        
        //mostrar resultado
        System.out.println("Ha introducido los números: " + n1 + " y " + n2);
        System.out.println("La suma de los números es: " + n1 + n2);
        System.out.println("La suma de los números es: " + (n1 + n2));
        sc.close();
    }
}