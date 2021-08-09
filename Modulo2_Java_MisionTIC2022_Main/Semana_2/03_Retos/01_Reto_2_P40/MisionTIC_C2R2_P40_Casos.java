//package  prueba;

public class MisionTIC_C2R2_P40_Casos {
    public static void main(String[] args) {
        
        // Pruebas Publicas
        Dispositivo dispositivos[]=new Dispositivo[3];
        dispositivos[0]=new Portatil(500.0, 3, 'E', 250);
        dispositivos[1]=new Tablet();
        dispositivos[2]=new Dispositivo(600.0, 3, 'D');
        PrecioTotal solucion1 = new PrecioTotal(dispositivos);
        solucion1.mostrarTotales();
        System.out.println("\n");
        
        
        Dispositivo dispositivos2[]=new Dispositivo[7];
        dispositivos2[0]=new Tablet(150.0, 1);
        dispositivos2[1]=new Portatil(500.0, 2,'E',500);
        dispositivos2[2]=new Dispositivo();
        dispositivos2[3]=new Portatil(250.0, 4);
        dispositivos2[4]=new Tablet(400.0, 3, 'A', 4);
        dispositivos2[5]=new Dispositivo(50.0, 3);
        PrecioTotal solucion2 = new PrecioTotal(dispositivos2);
        solucion2.mostrarTotales();
        System.out.println();

        
        
        // Pruebas Privadas
        Dispositivo dispositivos3[]=new Dispositivo[5];
        dispositivos3[0]=new Tablet(320.0, 1);
        dispositivos3[1]=new Portatil(350.0, 3);
        dispositivos3[2]=new Tablet(370.0, 2, 'A', 3);
        dispositivos3[3]=new Portatil(180.0, 2, 'E', 2000);
        dispositivos3[4]=new Dispositivo(50.0, 4);
        PrecioTotal solucion3 = new PrecioTotal(dispositivos3);
        solucion3.mostrarTotales();
        System.out.println();
        
        Dispositivo dispositivos4[]=new Dispositivo[10];
        dispositivos4[0]=new Tablet(320.0, 2);
        dispositivos4[1]=new Portatil(350.0, 2);
        dispositivos4[2]=new Tablet(370.0, 3, 'A', 3);
        dispositivos4[3]=new Portatil(180.0, 3);
        dispositivos4[4]=new Dispositivo(50.0, 2);
        dispositivos4[5]=new Tablet(300.0, 4, 'Z', 4);
        dispositivos4[6]=new Portatil(250.0, 2);
        dispositivos4[7]=new Tablet(400.0, 1, 'A', 2);
        dispositivos4[8]=new Portatil(200.0, 2);
        dispositivos4[9]=new Dispositivo(50.0, 1);
        PrecioTotal solucion4 = new PrecioTotal(dispositivos4);
        solucion4.mostrarTotales();
        System.out.println();
        
    }    
}

class PrecioTotal {
    private Double totalDispositivos = 0.0;
    private Double totalPortatiles = 0.0;
    private Double totalTablets = 0.0;
    private Dispositivo[] listaDispositivos;

    // Constructor
    PrecioTotal(Dispositivo[] pDispositivos) {
        this.listaDispositivos = pDispositivos;
    }

    public void mostrarTotales() {
        for (int i = 0; i < listaDispositivos.length; i++) {

            if (listaDispositivos[i] instanceof Dispositivo) {
                totalDispositivos += listaDispositivos[i].calcularPrecio();
            }
            if (listaDispositivos[i] instanceof Tablet) {
                totalTablets += listaDispositivos[i].calcularPrecio();
            }
            if (listaDispositivos[i] instanceof Portatil) {
                totalPortatiles += listaDispositivos[i].calcularPrecio();
            }
        }

        // Mostramos los resultados
        System.out.println("Total precios de dispositivos " + totalDispositivos);
        System.out.println("Total precios de computadores portátiles " + totalPortatiles);
        System.out.println("Total precios de tabletas " + totalTablets);
    }
}

class Dispositivo {
    protected final static char CONSUMO_W='F';
    protected final static Double PRECIO_BASE=100.0;
    protected final static Integer PESO_BASE=1;
    
    protected Double precioBase;
    protected char consumoW;
    protected Integer peso;

    //Constructores
    public Dispositivo(){
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W);
    }
   
    public Dispositivo(Double precioBase, Integer peso){
        this(precioBase, peso, CONSUMO_W);
    }
   
    public Dispositivo(Double precioBase, Integer peso, char consumoW){
        this.precioBase=precioBase;
        this.peso=peso;
        //System.out.println("entar aca");
        comprobarconsumoW(consumoW);
    }
   
    // Metodos
    public void comprobarconsumoW(char consumoW){
          
        if(consumoW>=2 && consumoW<=20){
            this.consumoW=consumoW;
        }else{
            this.consumoW=CONSUMO_W;
        }
          
    }

    public Double calcularPrecio(){
        Double adicion=0.0;
        switch(consumoW){
            case 'A':
                adicion+=100.0;
                break;
            case 'B':
                adicion+=80.0;
                break;
            case 'C':
                adicion+=60.0;
                break;
            case 'D':
                adicion+=50.0;
                break;
            case 'E':
                adicion+=30.0;
                break;
            case 'F':
                adicion+=10.0;
                break;
        }
   
        if(peso>1 && peso<=2){
            adicion+=10.0;
        }else if(peso>2 && peso<=3){
            adicion+=50.0;
        }else if(peso>3 && peso<=4){
            adicion+=80.0;
        }else if(peso>4){
            adicion+=100.0;
        }
   
        return precioBase+adicion;
    }

    public Double getPrecioBase() {
        return precioBase;
    }

    public char getconsumoW() {
        return consumoW;
    }

    public Integer getPeso() {
        return peso;
    }
}

class Tablet extends Dispositivo{
    private final static Integer MEMORIA_RAM_BASE=1;
    
    private Integer memoriaRam;
    
    //Constructor
    public Tablet(){
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W, MEMORIA_RAM_BASE);
    }
  
    public Tablet(Double precioBase, Integer peso){
        this(precioBase, peso, CONSUMO_W, MEMORIA_RAM_BASE);
    }
  
    public Tablet(Double precioBase, Integer peso, char consumoW, Integer memoriaRam){
        super(precioBase, peso, consumoW);
        this.memoriaRam=memoriaRam;
    
    }
  
    // Metodos
    public Double calcularPrecio(){
        Double adicion=super.calcularPrecio();
        if (memoriaRam > 1 && memoriaRam <=2){
            adicion+=5;
        }
        if (memoriaRam > 2 && memoriaRam <= 4){
            adicion+=25;
        }
        if (memoriaRam > 4){
            adicion+=50;
        }
  
        return adicion;
    }

    public Integer getMemoriaRam() {
        return memoriaRam;
    }

}

class Portatil extends Dispositivo{
    
    private final static Integer DISCO_DURO_BASE=250;
   
    private Integer discoDuro;
    

    //Constructor
    public Portatil(){
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W, DISCO_DURO_BASE);
    }
  
    public Portatil(Double precioBase, Integer peso){
        this(precioBase, peso, CONSUMO_W, DISCO_DURO_BASE);
    }

    public Portatil(Double precioBase, Integer peso, char consumoW, Integer discoDuro){
        
        super(precioBase, peso, consumoW);
        this.discoDuro=discoDuro;
        //System.out.println("entra1");
    }
  
    // Metodos
    public Double calcularPrecio(){
        Double adicion=super.calcularPrecio();
        
        if (discoDuro > 250 && discoDuro <= 500){
            adicion+=10;
        }
        if (discoDuro > 500 && discoDuro <= 1000){
            adicion+=50;
        }
        if (discoDuro > 1000){
            adicion+=100;
        }

        return adicion;
    }
}

