package model.vo;

public class MaterialRankeadoImportado {

    private Integer idMaterial;
    private String nombreMaterial;
    private Integer precioUnidad;    
    private String importado;

    public MaterialRankeadoImportado(){
    }

    public MaterialRankeadoImportado(Integer idMaterial, String nombreMaterial, Integer precioUnidad, String importado){
        this.idMaterial = idMaterial;
        this.nombreMaterial = nombreMaterial;
        this.precioUnidad = precioUnidad;
        this.importado = importado;
    }

    public Integer getIdMaterial() {
        return idMaterial;
    }

    public void setIdMaterial(Integer idMaterial) {
        this.idMaterial = idMaterial;
    }

    public String getNombreMaterial() {
        return nombreMaterial;
    }

    public void setNombreMaterial(String nombreMaterial) {
        this.nombreMaterial = nombreMaterial;
    }

    public Integer getPrecioUnidad() {
        return precioUnidad;
    }

    public void setPrecioUnidad(Integer precioUnidad) {
        this.precioUnidad = precioUnidad;
    }

    public String getImportado() {
        return importado;
    }

    public void setImportado(String importado) {
        this.importado = importado;
    }
}
