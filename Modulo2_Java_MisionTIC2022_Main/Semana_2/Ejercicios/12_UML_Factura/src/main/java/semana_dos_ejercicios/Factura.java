package semana_dos_ejercicios;

import java.util.*;

public class Factura extends Comprobante {
    private ArrayList<Producto> mProducto;
    private Float total;
    private Cliente mCliente;

    public Factura(){
    }
    
    public Factura(char t, int n, Fecha f, Cliente cli){
        super(t,n,f);
        setCliente(cli);
    }
    public void setTotal(Float val){
        this.total = val;
    }
    public void setCliente(Cliente val){
        this.mCliente = val;
    }
    public Cliente getCliente(){
        return mCliente;
    }
    public Float getTotal(){
        return total;
    }
    public ArrayList<Producto> getProducto(){
        return mProducto;
    }
    public void setProducto (ArrayList<Producto> val){
        this.mProducto = val;
    }
    public void agregarProducto(Producto p){
        mProducto.add(p);
        setTotal(getTotal() + p.getPrecio());
    }
    public void mostrarProductos(){
        Iterator<Producto> iter = mProducto.iterator();
        while (iter.hasNext()) {
            Producto p = iter.next();
            System.out.printf("Codigo: %d Descripcion: %s Precio: %5.2f \n",
            p.getCodigo(), p.getDescripcion(), p.getPrecio());
        }
    }
    public void mostrar(){
        System.out.printf("Tipo: %c Número: %d Fecha: %d/%d/%d\n",
        getTipo(), getNumero(),
        getFecha().getDia(), getFecha().getMes(), getFecha().getAno());
        System.out.printf("Cliente: \n");
        System.out.printf("Codigo: %d Razon Social: %s \n",
        mCliente.getCodigo(), mCliente.getRazonSocial());
        System.out.printf("Productos: \n");
        mostrarProductos();
        System.out.printf("Total: %6.2f \n",getTotal());
    }
}