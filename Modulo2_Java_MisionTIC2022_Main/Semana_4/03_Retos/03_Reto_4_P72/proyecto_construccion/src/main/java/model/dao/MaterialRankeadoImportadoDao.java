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
import model.vo.MaterialRankeadoImportado;

public class MaterialRankeadoImportadoDao {

    //Obtener los 10 materiales rankeados "si" son importados
    public ArrayList<MaterialRankeadoImportado> rankingMaterialesImportados() throws SQLException {

        ArrayList<MaterialRankeadoImportado> respuesta = new ArrayList<MaterialRankeadoImportado>();
        Connection conexion = JDBCUtilities.getConnection();

        try{       

            String consulta =   "SELECT ID_MaterialConstruccion, Nombre_Material, Precio_Unidad "+
                                        "FROM MaterialConstruccion "+
                                        "WHERE Importado = 'Si' "+
                                        "AND Precio_Unidad >= 2000 "+
                                        "ORDER BY ID_MaterialConstruccion ";

            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            //Recorrer los registros en los VO específicos
            while(resultSet.next()){
                MaterialRankeadoImportado materialRankeadoImportado = new MaterialRankeadoImportado();
                materialRankeadoImportado.setIdMaterial(resultSet.getInt("ID_MaterialConstruccion"));
                materialRankeadoImportado.setNombreMaterial(resultSet.getString("Nombre_Material"));
                materialRankeadoImportado.setPrecioUnidad(resultSet.getInt("Precio_Unidad"));

                //Se agrega cada registro como un objeto del ArrayList que contiene la consulta
                respuesta.add(materialRankeadoImportado);
            }

            resultSet.close();
            statement.close();

        }catch(SQLException e){
            System.err.println("Error consultando ranking de materiales si son importados : "+e);
        }finally{
            if(conexion != null){
                conexion.close();
            }
        }

        //Retornar la colección de vo's
        return respuesta;
    }  
}
