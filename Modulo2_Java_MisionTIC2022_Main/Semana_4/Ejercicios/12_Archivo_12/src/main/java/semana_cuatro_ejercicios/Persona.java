package semana_cuatro_ejercicios;

import java.io.*;

public class Persona implements Serializable {
    private String dni;
    private String nombre;
    private String apellidos;

    public Persona(String dni, String nombre, String apellidos) {
        this.dni = dni;
        this.nombre = nombre;
        this.apellidos = apellidos;
    }

    public String getDNI() {
        return this.dni;
    }

    public String getNombre() {
        return this.nombre;
    }

    public String getApellidos() {
        return this.apellidos;
    }

    public String getAtributos() {
        return this.getDNI() + " " + this.getApellidos() + ", " + this.getNombre();
    }

    public static void main(String[] args) {
        
        
        //FileReader fr = new FileReader ("Objeto.dat");
        //BufferedReader fd = new BufferedReader (fr);
        File nombre = new File("Objeto.dat");

        try{
            FileInputStream archivo = new FileInputStream(nombre);
            ObjectInputStream ois = new ObjectInputStream(archivo);
            Persona p1 = (Persona) ois.readObject();
            Persona p2 = (Persona) ois.readObject();
            ois.close();
            System.out.println("Cedula\t Nombre");
            System.out.println(p1.getAtributos());
            System.out.println(p2.getAtributos());
        }catch(FileNotFoundException e){
            System.out.println("¡El fichero no existe!");
        }catch(IOException e){
            System.out.println(e.getMessage());
        }catch(Exception e){
            System.out.println(e.getMessage());
        };
    }
}
