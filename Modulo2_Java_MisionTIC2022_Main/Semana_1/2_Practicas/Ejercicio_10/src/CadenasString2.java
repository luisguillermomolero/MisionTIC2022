// Programa que concatena cadenas de caracteres con el método concat()
public class CadenasString2 {
    
    public static void main(String[] args) {
        String nombre, apellido, domicilio, callePaseo;
 
        //inicializamos los String
        nombre="Pepe";
        apellido="Gotera";
        callePaseo="la calle";
        domicilio="Villabotijos de Abajo";
 
        System.out.println("Me llamo ".concat(nombre).concat(apellido).concat(" y vivo en ").concat(callePaseo).concat(domicilio));
        
    }    
}