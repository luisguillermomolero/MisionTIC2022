package model.dao;

//Estructura de datos
import java.util.ArrayList;

//Librerías para SQL y Base de Datos
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

//Clase para conexión
import util.JDBCUtilities;

//Encapsulamiento de los datos
import model.vo.LideresProyectosEmblematicos;

public class LideresProyectosEmblematicosDao {

    //Obtener los 9 "id_lideres", "id_proyecto" e "id_tipo"
    public ArrayList<LideresProyectosEmblematicos> rankingProyectosEmblematicos() throws SQLException {

        ArrayList<LideresProyectosEmblematicos> respuesta = new ArrayList<LideresProyectosEmblematicos>();
        Connection conexion = JDBCUtilities.getConnection();

        try{       

            String consulta =   "SELECT ID_Lider, ID_Proyecto, ID_Tipo "+
                                "FROM Proyecto "+
                                "WHERE ID_Proyecto >= 180 AND ID_Proyecto < 195 "+
                                "GROUP BY ID_Lider "+
                                "ORDER BY ID_Lider ";

            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            //Recorrer los registros en los VO específicos
            while(resultSet.next()){
                LideresProyectosEmblematicos lideresProyectosEmblematicos = new LideresProyectosEmblematicos();
                lideresProyectosEmblematicos.setIdLider(resultSet.getInt("Id_Lider"));
                lideresProyectosEmblematicos.setIdProyecto(resultSet.getInt("Id_Proyecto"));
                lideresProyectosEmblematicos.setIdTipo(resultSet.getInt("Id_Tipo"));

                //Se agrega cada registro como un objeto del ArrayList que contiene la consulta
                respuesta.add(lideresProyectosEmblematicos);
            }

            resultSet.close();
            statement.close();

        }catch(SQLException e){
            System.err.println("Error consultando ranking de los 10 proyectos con mayor gasto por compras: "+e);
        }finally{
            if(conexion != null){
                conexion.close();
            }
        }

        //Retornar la colección de vo's
        return respuesta;
    }  
}
