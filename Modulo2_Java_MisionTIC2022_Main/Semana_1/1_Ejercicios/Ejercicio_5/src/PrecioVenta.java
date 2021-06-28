//Programa que calcule el precio de venta de un producto conociendo el precio por unidad (sin IVA) del producto, el número de productos vendidos y el porcentaje de IVA aplicado. Los datos anteriores se leerán por teclado. 

import java.util.Scanner;

public class PrecioVenta {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double precioUnidad, cantidad, iva, precioSinIva, totalIva;

        System.out.print("Introduzca precio por unidad del producto: ");                                          
        precioUnidad = sc.nextDouble();

        System.out.print("Introduzca número de productos vendidos: ");
        cantidad = sc.nextDouble();

        System.out.print("Introduzca %IVA: ");
        iva = sc.nextDouble();

        precioSinIva = precioUnidad * cantidad;
        totalIva = precioSinIva * iva / 100;

        System.out.println("Precio de venta -> " + (precioSinIva + totalIva));                                    
    }
}