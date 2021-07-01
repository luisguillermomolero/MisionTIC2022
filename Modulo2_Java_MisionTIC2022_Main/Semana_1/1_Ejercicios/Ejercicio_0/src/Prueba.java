import java.util.Scanner; //Importa la clase Scanner

public class Prueba {
    public static void main(String[] args) {
        System.out.print("Hola Mundo \n");

        var sc = new Scanner(System.in); 
        System.out.println("Por favor ingrese su nombre");
        var nombre = sc.nextLine(); //nextInt(); nextFloat(); nextDouble();
        
        System.out.println("Hola " + nombre + "!");
        
        System.out.print("Por favor, introduzca un número :");
        int numero = sc.nextInt(); 
        
        //Cierre de Scanner
        sc.close();

        int i = 0;
        for (i = 0; i <= numero; i++){
            System.out.println("El For va de i = " + i + " hasta " + numero);
            if (i == numero){
                System.out.println("Hasta aquí llego el ejercicio");
            }
        }
        
        int n = 0;
        do{
            System.out.println("El do-while va de n = " + n + " hasta " + numero);
            n = n+1;
        } while(n <= numero);

        int s = 0;
        while (s <= numero){
            System.out.println("El while va de s = " + s + " hasta " + numero);
            s = s+1;
        }
    }
}