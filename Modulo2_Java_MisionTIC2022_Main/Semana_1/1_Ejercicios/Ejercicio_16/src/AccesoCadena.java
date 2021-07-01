// Programa que permite acceder a un caracter dentro de una cadena de caracteres.
// Para ello, se hace uso del método charAt(int index), donde el argumento es un valor entero

public class AccesoCadena {
 
    public static void main(String[] args) {
        String cadena = "Hola Pepe";
        char car1;
        car1 = cadena.charAt(5);
 
        System.out.println(car1); //Presentaria el caracter "P"
    }
    
}