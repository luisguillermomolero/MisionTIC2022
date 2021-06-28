// Programa para concatenar cadenas de caracteres
public class CadenasString {
    
    public static void main(String[] args) {
        String nombre, apellido, domicilio, callePaseo;
 
        //inicializamos los String
        nombre="Pepe";
        apellido="Gotera";
        callePaseo="la calle";
        domicilio="Villabotijos de Abajo";
 
        System.out.println("Me llamo " +nombre+" "+ " "+apellido+" y vivo en "+callePaseo+" "+domicilio);
 
        System.out.println();
 
        //Cuando la sentencia es muy larga hay que emplear el operador + y separar en lineas
         System.out.println("Me llamo " +nombre+" "
                 + " "+apellido+" y vivo en "
                 +callePaseo+" "+domicilio);        
    }    
}