//Alumno: Adrian F Perez
//Grupo: 40
//Profesor: Luis G Morelo

//Programa que solicita por teclado al menos 5 atributos de una persona y 
//imprimir por consola.

import java.util.Scanner;

public class ProbarPersona {
    public static void main(String[] args) throws Exception {
       
        Persona a = new Persona(); // Crear instancia o objeto "a"
        a.setNombre("Nombre: ");
        a.setApellido("Apellido: ");
        a.setEdad("Edad: ");
        a.setCedula("Cedula: ");
        a.setSexo("Sexo: 'H' ó 'M': ");
        a.mostrar();

    }

    public static class Persona{
        
        Scanner sc = new Scanner(System.in);

        private String nombre, apellido;
        private int edad, cedula;
        private char sexo;

        //contructor
        public Persona(){

        }

        public String getNombre(){
            return nombre;
        }

        public void setNombre(String txt){
            System.out.print(txt); //imprimir texto del main.
            nombre = sc.nextLine();
        }

        public String getApellido(){
            return apellido;
        }

        public void setApellido(String txt){
            System.out.print(txt);
            apellido = sc.nextLine();
        }

        public int getEdad(){
            return edad;
        }

        public void setEdad(String txt){
            System.out.print(txt);
            edad = sc.nextInt();
        }

        public int getCedula(){
            return cedula;
        }

        public void setCedula(String txt){
            System.out.print(txt);
            cedula = sc.nextInt();
        }

        public String getSexo(){
            String s = " ";
            if(sexo=='H') s="Hombre";
            if(sexo=='M') s="Mujer";
            if(sexo!='H' & sexo!='M') s="Desconocido";
            return s;
        }

        public void setSexo(String txt){
            System.out.print(txt);
            sexo = sc.next().charAt(0);
        }

        //imprimir en pantalla
        public void mostrar(){
            System.out.println("Nombre: " + nombre);
            System.out.println("Apellido: " + apellido);
            System.out.println("Edad: " + edad);
            System.out.println("Edad: " + cedula);
            System.out.println("Sexo: " + getSexo());
        }
    }
}
