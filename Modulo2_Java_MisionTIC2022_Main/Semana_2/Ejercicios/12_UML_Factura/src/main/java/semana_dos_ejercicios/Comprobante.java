package semana_dos_ejercicios;

public class Comprobante{

    private char tipo;
    private int numero;
    private Fecha fecha;
    
    public Comprobante(){
    }
    public Comprobante(char t, int n, Fecha f){
        setTipo(t);
        setNumero(n);
        setFecha(f);
    }
    public void setTipo(char val){
        this.tipo = val;
    }
    public void setNumero(int val){
        this.numero = val;
    }
    public void setFecha(Fecha val){
        this.fecha = val;
    }
    public char getTipo(){
        return tipo;
    }
    public int getNumero(){
        return numero;
    }
    public Fecha getFecha(){
        return fecha;
    }
}