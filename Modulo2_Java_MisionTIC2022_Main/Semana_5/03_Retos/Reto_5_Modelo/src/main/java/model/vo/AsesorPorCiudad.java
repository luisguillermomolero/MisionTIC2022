package model.vo;

public class AsesorPorCiudad {
    
    private Integer IdLider;
    private String nombre;
    private String primerApellido;
    private String ciudadResidencia;
    
    public AsesorPorCiudad() {
    }

    public AsesorPorCiudad(Integer idLider, String nombre, String primerApellido, String ciudadResidencia) {
        IdLider = idLider;
        this.nombre = nombre;
        this.primerApellido = primerApellido;
        this.ciudadResidencia = ciudadResidencia;
    }

    public Integer getIdLider() {
        return IdLider;
    }

    public void setIdLider(Integer idLider) {
        IdLider = idLider;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPrimerApellido() {
        return primerApellido;
    }

    public void setPrimerApellido(String primerApellido) {
        this.primerApellido = primerApellido;
    }

    public String getCiudadResidencia() {
        return ciudadResidencia;
    }

    public void setCiudadResidencia(String ciudadResidencia) {
        this.ciudadResidencia = ciudadResidencia;
    }


    
}
