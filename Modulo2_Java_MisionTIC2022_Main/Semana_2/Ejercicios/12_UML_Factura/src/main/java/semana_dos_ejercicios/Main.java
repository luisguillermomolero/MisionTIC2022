//Toda factura es un comprobante de venta, que debe poseer una fecha, el tipo de comprobante, un número, datos del cliente, los productos involucrados y un importe total.  En base al precio de los n productos que posee la factura se calcula el total.

package semana_dos_ejercicios;

public class Main {
    
    public static void main(String[] args) {
        Fecha hoy = new Fecha(20,10,2011);
        Producto pro1 = new Producto(1, "Cafe", (float) 8.5);
        Producto pro2 = new Producto(2, "Media Luna", 2);
        Cliente cliente = new Cliente(1, "Juana");
        Factura f1 = new Factura('F', 1, hoy, cliente);
        f1.agregarProducto(pro1);
        f1.agregarProducto(pro2);
        f1.mostrar();
 }
}