//Realizado por: Juan Carlos Cañon Sossa. Grupo P60

public class EnsayoString //se inicia la clase 
{
    public static void main(String args[])//método principal
    {
        //Declaración de String y métodos asociados
        var cadena = "El perro (Canis familiaris o Canis lupus familiaris) dependiendo de si se lo considera una especie por derecho propio o una subespecie del lobo";
        
        System.out.println(cadena);//muestre la cadena original
        System.out.println(cadena.length());//muestra la longitud de la cadena
        System.out.println(cadena.indexOf("p"));// muestra la posición de la primera letra p en la cadena
        System.out.println(cadena.charAt(3));//muestra la letra que hay en la posición 3
        System.out.println(cadena.substring(10,26));//muestra la subcadena entre la posición 10 y la 25
        System.out.println(cadena.toUpperCase());//convierte y muestra la cadena en mayúsculas
        System.out.println(cadena.toLowerCase());//convierte y muestra la cadena en minúsculas
    	System.out.println(cadena.trim());//muestra una copia de la cadena original
    }
}

