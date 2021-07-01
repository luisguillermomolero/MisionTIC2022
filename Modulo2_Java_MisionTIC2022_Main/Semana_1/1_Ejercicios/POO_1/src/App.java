// Miguel Alfonso Martinez Barragan Grupo P72

import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        client cliente = new client();
        System.out.println("Hello, World!");
        cliente.cedula("Ingrese su cedula...");
        cliente.nombre(" Ingrese su nombre...");
        cliente.direccion(" ingrese su dirección...");
        cliente.telefono(" Ingrese su telefono...");
        cliente.genero(" Ingrese su genero H o M");
        cliente.show();
    }
}

class client {
    Scanner sc = new Scanner(System.in);
    double id;
    String name;
    String address;
    double phone;
    String gender;

    public void cedula(String texto) {
        System.out.println(texto);
        id = Double.parseDouble((sc.nextLine()));
    }

    public void nombre(String texto) {
        System.out.println(texto);
        name = sc.nextLine();
    }

    public void direccion(String texto) {
        System.out.println(texto);
        address = sc.nextLine();
    }

    public void telefono(String texto) {
        System.out.println(texto);
        phone = Double.parseDouble(sc.nextLine());
    }

    public void genero(String texto) {
        System.out.println(texto);
        gender = sc.nextLine();
    }

    public void show() {
        System.out.println("Datos de Cliente");
        System.out.println("Cedula      : " + id);
        System.out.println("Nombre      : " + name);
        System.out.println("Dirección   : " + address);
    }
}

