// Realizado Michael Sebastian Herrera Cristiano. Grupo P72

import java.util.Scanner;
class libro{
    String numero;
    String nombre;
    String tipo;
    String autor;
    int año;

    public void id( String dato){
        this.numero = dato;
    }
    public void nombre( String dato){
        this.numero = dato;
    }
    public void tipo( String dato){
        this.tipo = dato;
    }
    public void autor( String dato){
        this.autor = dato;
    }

    public void imprimir (){

        System.out.println("Numero: "+numero+"\n"+"Nombre:"+nombre+"\n"+"tipo: "+tipo+"\n"+"autor: "+autor);
    }
}

public class App {
    public static void main(String[] args) throws Exception {
        libro lb = new libro();
        
        Scanner sc = new Scanner(System.in);
        System.out.println("escriba numero de libro");
        lb.id(sc.nextLine());
        System.out.println("Nombre: ");
        lb.nombre(sc.nextLine());
        System.out.println("tipo: ");
        lb.tipo(sc.nextLine());
        System.out.println("autor: ");
        lb.autor(sc.nextLine());
   
        lb.imprimir();
        sc.close();
    }
}
