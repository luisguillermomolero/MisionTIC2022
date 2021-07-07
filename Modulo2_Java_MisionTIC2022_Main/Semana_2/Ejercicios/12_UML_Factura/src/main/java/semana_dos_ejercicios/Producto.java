package semana_dos_ejercicios;

public class Producto {
    private int codigo;
    private String descripcion;
    private Float precio;

    public Producto(){
    }
    public Producto(int c, String d, float p){
        setCodigo(c);
        setDescripcion(d);
        setPrecio(p);
    }
    public void setCodigo(int val){
        this.codigo = val;
    }
    public void setDescripcion(String val){
        this.descripcion = val;
    }
    public void setPrecio(Float val){
        this.precio = val;
    }
    public int getCodigo(){
        return codigo;
    }
    public String getDescripcion(){
        return descripcion;
    }
    public Float getPrecio(){
        return precio;
    }
}