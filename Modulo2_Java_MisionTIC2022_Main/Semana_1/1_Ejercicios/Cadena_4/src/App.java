// Diana Pinzón Torres. Grupo P60

public class App {   
    public static void main(String[] args) {       
        int longitud; 
        // declara la cadena como un objeto S1       
        String S1 = "El perro (Canis familiaris o Canis lupus familiaris dependiendo de si se lo considera una especie por derecho propio o una subespecie del lobo";
        // Calculo de la longitud     
        System.out.println("Longitud de una cadena es:" + S1.length());
        // Busqueda de la primera posición donde aparece la letra C    
        System.out.println("La primera posición donde aparece la letra C es:" + S1.indexOf('C'));
        // Calculo de la longitud    
        System.out.println("El caracter de la posición 20 es: " + S1.charAt(20));
        // Busqueda del texto contenido entre dos posiciones para este caso 0 y 15    
        System.out.println("El tesxto contenodo entre la posición 0 y la 15 es:" + S1.substring(0,15));
        // Conversión del texto en mayuscula sostenida   
        System.out.println("El texto en minúscula sostenida se ve así:"  + S1.toUpperCase());
        // Conversión del texto en minuscula sostenida    
        System.out.println("El texto en minúscula sostenida se ve así:"  + S1.toLowerCase());
        // Eliminación de ls espacios en blanco en el texto  
        System.out.println("El texto sin espacios en blanco se ve así:"  + S1.trim());
    }
}
