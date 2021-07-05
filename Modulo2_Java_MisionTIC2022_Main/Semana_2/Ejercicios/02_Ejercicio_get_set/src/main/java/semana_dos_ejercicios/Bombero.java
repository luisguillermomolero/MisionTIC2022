package semana_dos_ejercicios;

//clase bombero
public class Bombero{

    //Declaracion de variables (Atributos, propiedades)
    private String nombre;
    private String apellido;
    private int edad;

    //contructor y parametros asignados
    public Bombero(){
    }

    public Bombero (String nombreRecibido, String apellidoRecibido, int edadRecibida)
    {
        nombre = nombreRecibido;
        apellido = apellidoRecibido;
        edad = edadRecibida;
    }//cierre del constructor

    //Descriptor de mutación setter.  Leer variables de clase
    public void setNombre(String valorNombre){
        nombre = valorNombre;   
    }
    public void setApellido (String valorApellido){
        apellido = valorApellido;
    }
    public void setEdad(int valorEdad){
        edad = valorEdad;
    }

    //Descriptor de acceso getter. Cambiar contenidos de las variables de clase
    public String getNombre(){
        return nombre;
    }
    public String getApellido(){
        return apellido;
    }
    public int getEdad(){
        return edad;
    }

    public static void main(String[] args) {
        Bombero bomber = new Bombero("Luis", "Molero", 45);
        System.out.println("El registro es: \n * Nombre: " + bomber.getNombre()+ " * Apellido: " + bomber.getApellido() + " * Edad: "+ bomber.getEdad());
    }
}