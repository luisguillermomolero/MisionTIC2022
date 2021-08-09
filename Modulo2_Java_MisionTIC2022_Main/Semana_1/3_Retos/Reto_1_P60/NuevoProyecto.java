/**
 *  Ciclo 2 Reto 1 
*/
package utp.misiontic2022.c2.mundo;

/**
 * Clase que representa un Proyecto.
 */
public class NuevoProyecto {

	// -----------------------------------------------------------------
    // Atributos
    // -----------------------------------------------------------------

    /**
     * Nombre del proyecto.
     */
	private String proyecto;

	/**
     * Valor del Tiempo en meses.
     */
     private int periodo;
    
    /**
     * Valor del monto.
     */
    private double monto;
	
    /**
     * Tasa de interes efectiva mensual del proyecto 
     */
    private double interes;
	
	// -----------------------------------------------------------------
    // Métodos
    // -----------------------------------------------------------------

    /**
     * Construye el proyecto. <br>
     * <b>post: </b> Se creó un nuevo proyecto con los siguientes valores: <br>
     * Proyecto: UTP.
     */
	public NuevoProyecto()
    {
		 
		this.periodo = 0;
        this.monto = 0;
        this.interes= 0;
    }

    public NuevoProyecto(Integer periodo, double monto, double interes )
    {
	  
		this.periodo = periodo;
        this.monto = monto;
        this.interes= interes;
    }

	/**
     * Retorna el interes simple, monto, monto en una cadena de texto.
     * @return El total de interes simples generados en número.
     */
    public double calcularInteresSimple( )
    {
        double interesSimple= this.monto * (this.interes /100) * this.periodo;

        return Math.round(interesSimple);
    }
    
    
    /**
     * Retorna el interes compuesto, monto, monto en una cadena de texto.
     * @return El total de interes compuestos generados en número.
     */
    public double calcularInteresCompuesto( )
    {
        double interesCompuesto= this.monto * (Math.pow(1 + (this.interes /100), this.periodo) -1);

        return Math.round(interesCompuesto);
    }
    
    /**
     * Método para comparar la diferencia en el total de intereses generados para el proyecto.
     * @return Respuesta al Reto.
     */
    public double compararInversion ( int pPeriodo, double pMonto, double pInteres )
    {
    	periodo = pPeriodo;
        monto = pMonto;
        interes = pInteres;

        double diferencia = 0;
        
        /* Cálculo de la diferencia entre tipos de tasas */
    	diferencia = calcularInteresCompuesto() - calcularInteresSimple();

    	return diferencia;
    	
    }

    public double compararInversion ( )
    {
        double diferencia = 0;
        
        /* Cálculo de la diferencia entre tipos de tasas */
    	diferencia = calcularInteresCompuesto( ) - calcularInteresSimple( );
    	
    	return diferencia;
    }

    public static void main(String[] args){
        //Caso de prueba 1
        NuevoProyecto np = new NuevoProyecto();
        System.out.println(np.calcularInteresSimple());
        System.out.println(np.calcularInteresCompuesto());
        System.out.println(np.compararInversion(6,10000000,1.2));

        //Caso de prueba 2
        System.out.println("\n");
        NuevoProyecto np2 = new NuevoProyecto(6,10000000,1.2);
        System.out.println(np2.calcularInteresSimple());
        System.out.println(np2.calcularInteresCompuesto());
        System.out.println(np2.compararInversion());

        //Caso de prueba 3
        System.out.println("\n");
        NuevoProyecto np3 = new NuevoProyecto();
        System.out.println(np3.calcularInteresSimple());
        System.out.println(np3.calcularInteresCompuesto());
        System.out.println(np3.compararInversion(24,6000000,1.9));

        //Caso de prueba 4
        System.out.println("\n");
        NuevoProyecto np4 = new NuevoProyecto(12,10000000,0.9);
        System.out.println(np4.calcularInteresSimple());
        System.out.println(np4.calcularInteresCompuesto());
        System.out.println(np4.compararInversion());

    }
}

