package model.vo;

public class ProyectosCasaCampestre {
    private Integer ID_Proyecto;
    private String Constructora; 
    private Double Numero_Habitaciones;
    private String Ciudad;
    
    public ProyectosCasaCampestre() {
    }

    public ProyectosCasaCampestre(Integer iD_Proyecto, String constructora, Double numero_Habitaciones, String ciudad) {
        ID_Proyecto = iD_Proyecto;
        Constructora = constructora;
        Numero_Habitaciones = numero_Habitaciones;
        Ciudad = ciudad;
    }

    public Integer getID_Proyecto() {
        return ID_Proyecto;
    }

    public void setID_Proyecto(Integer iD_Proyecto) {
        ID_Proyecto = iD_Proyecto;
    }

    public String getConstructora() {
        return Constructora;
    }

    public void setConstructora(String constructora) {
        Constructora = constructora;
    }

    public Double getNumero_Habitaciones() {
        return Numero_Habitaciones;
    }

    public void setNumero_Habitaciones(Double numero_Habitaciones) {
        Numero_Habitaciones = numero_Habitaciones;
    }

    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String ciudad) {
        Ciudad = ciudad;
    }

    
}
