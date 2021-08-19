package controller;

//Estructuras de datos (colecciones)
import java.util.ArrayList;

//Modelos (acceso y objetos contenedores)
import model.dao.AsesorPorCiudadDao;
import model.dao.CompraPorProveedorDao;
import model.dao.ProyectosCasaCampestreDao;
import model.vo.AsesorPorCiudad;
import model.vo.CompraPorProveedor;
import model.vo.ProyectosCasaCampestre;


//Librerías para bases de datos
import java.sql.SQLException;

public class ControladorRequerimientosReto4 {       
    
    private final CompraPorProveedorDao compraPorProveedorDao;
    private final ProyectosCasaCampestreDao proyectosCasaCampestreDao;
    private final AsesorPorCiudadDao asesorPorCiudadDao;
    
    public ControladorRequerimientosReto4(){
        this.compraPorProveedorDao = new CompraPorProveedorDao();
        this.asesorPorCiudadDao = new AsesorPorCiudadDao();
        this.proyectosCasaCampestreDao = new ProyectosCasaCampestreDao();

    }

    public ArrayList<AsesorPorCiudad> consultarAsesorPorCiudad() throws SQLException {
        return this.asesorPorCiudadDao.rankingAsesorPorCiudad();
    }
    
    public ArrayList<CompraPorProveedor> consultarCompraPorProveedor() throws SQLException {
        return this.compraPorProveedorDao.rankingCompraPorProveedor();
    }

    public ArrayList<ProyectosCasaCampestre> consultarProyectosCasaCampestre() throws SQLException {
        return this.proyectosCasaCampestreDao.rankingProyectosCasaCampestres();
    }

}
