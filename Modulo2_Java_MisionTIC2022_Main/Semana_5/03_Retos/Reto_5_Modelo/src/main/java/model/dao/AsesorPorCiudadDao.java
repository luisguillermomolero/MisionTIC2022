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
import model.vo.AsesorPorCiudad;

public class AsesorPorCiudadDao {
    //Obtener los proyectos por Tipo en la ciudad de 
    public ArrayList<AsesorPorCiudad> rankingAsesorPorCiudad() throws SQLException {

        ArrayList<AsesorPorCiudad> respuesta = new ArrayList<AsesorPorCiudad>();
        Connection conexion = JDBCUtilities.getConnection();

        try{       

            String consulta =   "SELECT ID_Lider, Nombre, Primer_Apellido, Ciudad_Residencia "+
                                "FROM Lider "+
                                "WHERE Cargo = 'Asesor'"+
                                "ORDER BY Ciudad_Residencia ASC";


            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            //Recorrer los registros en los VO específicos
            while(resultSet.next()){
                AsesorPorCiudad asesorPorCiudad = new AsesorPorCiudad();
                asesorPorCiudad.setIdLider(resultSet.getInt("ID_Lider"));
                asesorPorCiudad.setNombre(resultSet.getString("Nombre"));
                asesorPorCiudad.setPrimerApellido(resultSet.getString("Primer_Apellido"));
                asesorPorCiudad.setCiudadResidencia(resultSet.getString("Ciudad_Residencia"));

                //Se agrega cada registro como un objeto del ArrayList que contiene la consulta
                respuesta.add(asesorPorCiudad);
            }

            resultSet.close();
            statement.close();

        }catch(SQLException e){
            System.err.println("Error consultando los proyectos de tipo Apartaestudio en Quibdo: "+e);
        }finally{
            if(conexion != null){
                conexion.close();
            }
        }

        //Retornar la colección de vo's
        return respuesta;
    }     
}
