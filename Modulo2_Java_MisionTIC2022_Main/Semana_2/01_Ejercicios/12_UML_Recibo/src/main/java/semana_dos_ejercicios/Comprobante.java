package semana_dos_ejercicios;

public class Comprobante {

    private String tipo;
    private int numero;
    private Fecha fecha;

    //Constructor
    public Comprobante(){
    }

    //Constructor
    public Comprobante (int dia, int mes, int anio) {
        fecha = new Fecha(dia, mes, anio);
    }
    
    //setter
    public void setTipo(String val){
        this.tipo = val;
    }
    public void setNumero(int val){
        this.numero = val;
    }
    public void setFecha(Fecha val){
        this.fecha= val;
    }

    //getter
    public String getTipo(){
        return tipo;
    }
    public int getNumero(){
        return numero;
    }
    public Fecha getFecha(){
        return fecha;
    }
}
