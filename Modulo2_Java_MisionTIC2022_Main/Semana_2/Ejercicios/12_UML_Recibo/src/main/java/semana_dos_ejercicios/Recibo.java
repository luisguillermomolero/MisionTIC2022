package semana_dos_ejercicios;

public class Recibo extends Comprobante{

    private Proveedor proveedor;
    private float total;
    private String detalle;

    public Recibo(){
    }
    public Recibo (int dia,int mes,int anio, String razonSocial, int codigo) {
        super(dia, mes, anio); // ejecuta el constructor de la superclase
        proveedor = new Proveedor(razonSocial, codigo);
    }
    public void setTotal(float val){
        this.total = val;
    }
    public void setDetalle(String val){
        this.detalle = val;
    }
    public void setProveedor(Proveedor val){
        this.proveedor = val;
    }
    public Float getTotal(){
        return total;
    }
    public String getDetalle(){
        return detalle;
    }
    public Proveedor getProveedor(){
        return proveedor;
    }
    public void Mostrar(){
        System.out.println("Tipo: " + getTipo() + " Número: " + getNumero());
        System.out.println("Fecha: " + getFecha());
        System.out.print("Proveedor código");
        System.out.println("Servicio Detalle:"+ getDetalle() + ".  Importe total: "+getTotal());
    }
}

/** Salida deseada
 * Tipo : R  Número: 1
 * Fecha: 27/10/2011
 * Proveedor Código: 2023, Razón Social: DeNada. S.A. 
 * Servicio Detalle: Pago servicios mensajeria. Total: 5000
 * */ 
