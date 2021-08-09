//Librerías
import java.util.ArrayList;
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

//Vista
public class VistaRequerimientosReto4 {
    
    public static final ControladorRequerimientosReto4 controlador = new ControladorRequerimientosReto4();

     public static void requerimiento1(){

        System.out.println("*** Lideres con mayor salario ***");       

        try{

            ArrayList<LideresMayorSalario> rankingLideresMayorSalario = controlador.consultarLideresMayorSalarios();

            //Encabezado del resultado
            System.out.println("ID_Lider  Nombre  Primer_Apellido");
            
            //Cada VO cargado, mostrarlo en la vista
            for (LideresMayorSalario lideresMayors : rankingLideresMayorSalario) {
                System.out.printf("      %d  %s   %s  %n", 
                    lideresMayors.getIdLider(), 
                    lideresMayors.getNombre(),
                    lideresMayors.getPrimerApellido()
                );   
            }

        }catch(SQLException e){
            System.err.println("Ha ocurrido un error!"+e.getMessage());
        }

    }

    public static void requerimiento3(){

        System.out.println("*** Lideres proyectos emblemáticos ***");       

        try{

            ArrayList<LideresProyectosEmblematicos> rankingProyectosEmblematicos = controlador.consultarLideresProyectosEmblematicos();

            //Encabezado del resultado
            System.out.println("Id_Lider Id_Proyecto Id_Tipo");
            
            //Cada VO cargado, mostrarlo en la vista
            for (LideresProyectosEmblematicos lideresProyectosE : rankingProyectosEmblematicos) {
                System.out.printf("      %d         %d       %d %n",
                    lideresProyectosE.getIdLider(),
                    lideresProyectosE.getIdProyecto(),
                    lideresProyectosE.getIdTipo()
                );   
            }

        }catch(SQLException e){
            System.err.println("Ha ocurrido un error!"+e.getMessage());
        }

    }

    public static void requerimiento4(){

        System.out.println("*** Productos importados ***");       

        try{
            
            ArrayList<MaterialRankeadoImportado> rankingMaterialesImportados = controlador.consultarMaterialesRankeadosImportados();

            //Cada VO cargado, mostrarlo en la vista
            for (MaterialRankeadoImportado materialImportado : rankingMaterialesImportados) {
                System.out.printf("El producto de ID %d de descripción: %s de tipo importado(a), tiene un precio de %d %n",
                    materialImportado.getIdMaterial(),
                    materialImportado.getNombreMaterial(),
                    materialImportado.getPrecioUnidad()
                );   
            }

        }catch(SQLException e){
            System.err.println("Ha ocurrido un error!"+e.getMessage());
        }
    }
}

//Controlador
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

//DAO's
public class LideresMayorSalarioDao {

    //Obtener los 10 proyectos rankeados según las compras
    public ArrayList<LideresMayorSalario> rankingLideresMayorSalario() throws SQLException {

        ArrayList<LideresMayorSalario> respuesta = new ArrayList<LideresMayorSalario>();
        Connection conexion = JDBCUtilities.getConnection();

        try{       

            String consulta =   "SELECT ID_Lider, Nombre, Primer_Apellido "+
                                "FROM Lider "+
                                "WHERE Salario >= 300000 AND Ciudad_Residencia = 'Barranquilla' "+
                                "ORDER BY ID_Lider ";

            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            //Recorrer los registros en los VO específicos
            while(resultSet.next()){
                LideresMayorSalario lideresMayorSalario = new LideresMayorSalario();
                lideresMayorSalario.setIdLider(resultSet.getInt("Id_Lider"));
                lideresMayorSalario.setNombre(resultSet.getString("Nombre"));
                lideresMayorSalario.setPrimerApellido(resultSet.getString("Primer_Apellido"));

                //Se agrega cada registro como un objeto del ArrayList que contiene la consulta
                respuesta.add(lideresMayorSalario);
            }

            resultSet.close();
            statement.close();

        }catch(SQLException e){
            System.err.println("Error consultando ranking de los lideres con mayor: "+e);
        }finally{
            if(conexion != null){
                conexion.close();
            }
        }

        //Retornar la colección de vo's
        return respuesta;
    }  
}

public class LideresProyectosEmblematicosDao {

    //Obtener los 9 "id_lideres", "id_proyecto" e "id_tipo"
    public ArrayList<LideresProyectosEmblematicos> rankingProyectosEmblematicos() throws SQLException {

        ArrayList<LideresProyectosEmblematicos> respuesta = new ArrayList<LideresProyectosEmblematicos>();
        Connection conexion = JDBCUtilities.getConnection();

        try{       

            String consulta =   "SELECT ID_Lider, ID_Proyecto, ID_Tipo "+
                                "FROM Proyecto "+
                                "WHERE ID_Proyecto >= 130 AND ID_Proyecto < 135 "+
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

public class MaterialRankeadoImportadoDao {

    //Obtener los 10 materiales rankeados "si" son importados
    public ArrayList<MaterialRankeadoImportado> rankingMaterialesImportados() throws SQLException {

        ArrayList<MaterialRankeadoImportado> respuesta = new ArrayList<MaterialRankeadoImportado>();
        Connection conexion = JDBCUtilities.getConnection();

        try{       

            String consulta =   "SELECT ID_MaterialConstruccion, Nombre_Material, Precio_Unidad "+
                                        "FROM MaterialConstruccion "+
                                        "WHERE Importado = 'Si' "+
                                        "AND Precio_Unidad >= 1800 "+
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

//VO's
public class LideresMayorSalario {

    private Integer idLider;
    private String nombre;
    private String primerApellido;
    private Integer salario;
    private String ciudadNacimiento;

    public LideresMayorSalario() {
    }

    public LideresMayorSalario(Integer idLider, String nombre, String primerApellido, Integer salario, String ciudadNacimiento) {
        this.idLider = idLider;
        this.nombre = nombre;
        this.primerApellido = primerApellido;
        this.salario = salario;
        this.ciudadNacimiento = ciudadNacimiento;
    }

    public Integer getIdLider() {
        return idLider;
    }

    public void setIdLider(Integer idLider) {
        this.idLider = idLider;
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

    public Integer getSalario() {
        return salario;
    }

    public void setSalario(Integer salario) {
        this.salario = salario;
    }

    public String getCiudadNacimiento() {
        return ciudadNacimiento;
    }

    public void setCiudadNacimiento(String ciudadNacimiento) {
        this.ciudadNacimiento = ciudadNacimiento;
    }
}

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

//JDBCUtilities 
public class JDBCUtilities {

    //Atributos de clase para gestión de conexión con la base de datos    
    private static final String UBICACION_BD = "ProyectosConstruccion.db";    

    public static Connection getConnection() throws SQLException {
        String url = "jdbc:sqlite:" + UBICACION_BD;        
        return DriverManager.getConnection(url);
    }

    public static boolean estaVacia(){
        File archivo = new File(JDBCUtilities.UBICACION_BD);
        return archivo.length() == 0;
    }
}
