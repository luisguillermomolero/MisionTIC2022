package semana_dos_ejercicios; //nombre del package

//import 
//import

public class Recibo extends Comprobante{  //Definicion clara de la clase/subclase

    //Atributos
    private Proveedor proveedor;
    private float total;
    private String detalle;

    //Constructor
    public Recibo(){
    }

    //Constructor
    public Recibo (int dia,int mes,int anio, String razonSocial, int codigo) {
        super(dia, mes, anio); // ejecuta el constructor de la superclase
        proveedor = new Proveedor(razonSocial, codigo);
    }

    //setter
    public void setTotal(float val){
        this.total = val;
    }
    public void setDetalle(String val){
        this.detalle = val;
    }
    public void setProveedor(Proveedor val){
        this.proveedor = val;
    }

    //getter
    public Float getTotal(){
        return total;
    }
    public String getDetalle(){
        return detalle;
    }
    public Proveedor getProveedor(){
        return proveedor;
    }
    
    //Método
    public void Mostrar(){
        System.out.println("Tipo: " + getTipo() + " Número: " + getNumero());
        System.out.println("Fecha: " + getFecha());
        System.out.print("Proveedor código");
        System.out.println("Servicio Detalle:"+ getDetalle() + ".  Importe total: "+getTotal());
    }
}