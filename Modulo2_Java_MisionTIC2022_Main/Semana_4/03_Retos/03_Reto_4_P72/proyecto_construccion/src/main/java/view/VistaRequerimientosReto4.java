package view;

import controller.ControladorRequerimientosReto4;
import model.vo.LideresMayorSalario;
import model.vo.LideresProyectosEmblematicos;
import model.vo.MaterialRankeadoImportado;

import java.sql.SQLException;
import java.util.ArrayList;

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
