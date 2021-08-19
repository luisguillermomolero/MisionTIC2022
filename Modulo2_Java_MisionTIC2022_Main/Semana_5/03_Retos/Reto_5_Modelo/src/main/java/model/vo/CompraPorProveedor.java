package model.vo;

public class CompraPorProveedor {
    
    private Integer ID_Compra;
    private String Proveedor;
    private String Constructora;
    private String Banco_Vinculado;
    private String Ciudad;
    
    public CompraPorProveedor() {
    }

    public CompraPorProveedor(Integer iD_Compra, String proveedor, String constructora, String banco_Vinculado,
            String ciudad) {
        ID_Compra = iD_Compra;
        Proveedor = proveedor;
        Constructora = constructora;
        Banco_Vinculado = banco_Vinculado;
        Ciudad = ciudad;
    }

    public Integer getID_Compra() {
        return ID_Compra;
    }

    public void setID_Compra(Integer iD_Compra) {
        ID_Compra = iD_Compra;
    }

    public String getProveedor() {
        return Proveedor;
    }

    public void setProveedor(String proveedor) {
        Proveedor = proveedor;
    }

    public String getConstructora() {
        return Constructora;
    }

    public void setConstructora(String constructora) {
        Constructora = constructora;
    }

    public String getBanco_Vinculado() {
        return Banco_Vinculado;
    }

    public void setBanco_Vinculado(String banco_Vinculado) {
        Banco_Vinculado = banco_Vinculado;
    }

    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String ciudad) {
        Ciudad = ciudad;
    }
    
    
}
