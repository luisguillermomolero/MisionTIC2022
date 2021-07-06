package semana_dos_ejercicios;

public class Proveedor {

    private int codigo;
    private String razonSocial;

    public Proveedor(){
    }
    public Proveedor (String razonSocial, int codigo) {
        setRazonSocial(razonSocial);
        setCodigo(codigo);
    }
    public void setCodigo(int val){
        this.codigo = val;
    }
    public void setRazonSocial(String val){
        this.razonSocial = val;
    }
    public int getCodigo(){
        return codigo;
    }
    public String getRazonSocial(){
        return razonSocial;
    }
}
