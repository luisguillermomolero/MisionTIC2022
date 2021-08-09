//Un enumerado (o Enum) es una clase "especial" que limita la creación de objetos a los especificados explícitamente en la implementación de la clase. La única limitación que tienen los enumerados respecto a una clase normal es que si tiene constructor, este debe de ser privado para que no se puedan crear nuevos objetos.

package semana_dos_ejercicios;

public enum Equipo
{
	BARÇA("FC Barcelona",1), REAL_MADRID("Real Madrid",2),
	SEVILLA("Sevilla FC",4), VILLAREAL("Villareal",7); 
	
	private String nombreClub;
	private int puestoLiga;
	
	public enum Demarcacion{
		//Los nombres de los enum se colocan en mayúscula
		PORTERO, DEFENSA, CENTROCAMPISTA, DELANTERO
	}

	//setter
	private Equipo (String nombreClub, int puestoLiga){
		this.nombreClub = nombreClub;
		this.puestoLiga = puestoLiga;
	}

	//getter
	public String getNombreClub() {
		return nombreClub;
	}
	public int getPuestoLiga() {
		return puestoLiga;
	}	
	
    public static void main(String[] args) {
        Demarcacion delantero = Demarcacion.DELANTERO; 
		Demarcacion defensa = Demarcacion.DEFENSA;
		
		// Devuelve un String con el nombre de la constante
		System.out.println("delantero.name()= "+delantero.name());
		System.out.println("defensa.toString()= "+defensa.toString());

		//  Devuelve un entero con la posición de la constante según está declarada.
		System.out.println("delantero.ordinal()= "+delantero.ordinal());

		// Compara el enum con el parámetro según el orden en el que están declaradas las constantes. 
		System.out.println("delantero.compareTo(portero)= "+delantero.compareTo(defensa));
		System.out.println("delantero.compareTo(delantero)= "+delantero.compareTo(delantero));

		// Recorre todas las constantes de la enumeración
		for(Demarcacion d: Demarcacion.values()){
			System.out.println(d.toString()+" - ");
		}
		
		// Instanciamos el enumerado
		Equipo villareal = Equipo.VILLAREAL;
		
		// Devuelve un String con el nombre de la constante
		System.out.println("villareal.name()= "+villareal.name());
		
		// Devuelve el contenido de los atributos
		System.out.println("villareal.getNombreClub()= "+villareal.getNombreClub());
		System.out.println("villareal.getPuestoLiga()= "+villareal.getPuestoLiga());
    }
}