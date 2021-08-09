package controller;

//Estructuras de datos (colecciones)
import java.util.ArrayList;

//Modelos (acceso y objetos contenedores)
import model.dao.LideresMayorSalarioDao;
import model.vo.LideresMayorSalario;
import model.dao.LideresProyectosEmblematicosDao;
import model.vo.LideresProyectosEmblematicos;
import model.dao.MaterialRankeadoImportadoDao;
import model.vo.MaterialRankeadoImportado;

//Librerías para bases de datos
import java.sql.SQLException;

public class ControladorRequerimientosReto4 {       
    
    private final LideresMayorSalarioDao lideresMayorSalarioDao;
    private final LideresProyectosEmblematicosDao lideresProyectosEmblematicosDao;
    private final MaterialRankeadoImportadoDao materialRankeadoImportadoDao;

    public ControladorRequerimientosReto4(){
        this.lideresMayorSalarioDao = new LideresMayorSalarioDao();
        this.lideresProyectosEmblematicosDao = new LideresProyectosEmblematicosDao();       
        this.materialRankeadoImportadoDao = new MaterialRankeadoImportadoDao();
    }

    public ArrayList<LideresMayorSalario> consultarLideresMayorSalarios() throws SQLException {
        return this.lideresMayorSalarioDao.rankingLideresMayorSalario();
    }
    
    public ArrayList<LideresProyectosEmblematicos> consultarLideresProyectosEmblematicos() throws SQLException {
        return this.lideresProyectosEmblematicosDao.rankingProyectosEmblematicos();
    }

    public ArrayList<MaterialRankeadoImportado> consultarMaterialesRankeadosImportados() throws SQLException {
        return this.materialRankeadoImportadoDao.rankingMaterialesImportados();
    }
}
