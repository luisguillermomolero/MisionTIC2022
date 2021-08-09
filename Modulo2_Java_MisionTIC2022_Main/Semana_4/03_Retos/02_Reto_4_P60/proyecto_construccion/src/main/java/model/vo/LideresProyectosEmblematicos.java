package model.vo;

public class LideresProyectosEmblematicos {

    private Integer idLider;
    private Integer idProyecto;
    private Integer idTipo;

    public LideresProyectosEmblematicos(){
        
    }

    public LideresProyectosEmblematicos(Integer idLider, Integer idProyecto, Integer idTipo){
        this.idLider = idLider;
        this.idProyecto = idProyecto;
        this.idTipo = idTipo;
    }

    public Integer getIdLider() {
        return idLider;
    }

    public void setIdLider(Integer idLider) {
        this.idLider = idLider;
    }

    public Integer getIdProyecto() {
        return idProyecto;
    }

    public void setIdProyecto(Integer idProyecto) {
        this.idProyecto = idProyecto;
    }

    public Integer getIdTipo() {
        return idTipo;
    }

    public void setIdTipo(Integer idTipo) {
        this.idTipo = idTipo;
    }
}
