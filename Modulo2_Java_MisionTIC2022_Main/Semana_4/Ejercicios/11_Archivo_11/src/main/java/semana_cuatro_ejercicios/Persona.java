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
    
        File nombre = new File("Objeto.dat");
        try{

            FileOutputStream archivo = new FileOutputStream(nombre);
            ObjectOutputStream oos = new ObjectOutputStream(archivo);
            oos.writeObject(new Persona("552871883", "María", "Ruiz Ramos"));
            oos.writeObject(new Persona("403020104", "Juan", "González López"));
            System.out.println("Archivo escrito");
            oos.close();
            }catch(FileNotFoundException e){
                System.out.println("¡El fichero no existe!");
            }catch(IOException e){
                System.out.println(e.getMessage());
            }catch(Exception e){
                System.out.println(e.getMessage());
        };    
    };
}

    

    