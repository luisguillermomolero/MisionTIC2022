package semana_dos_ejercicios;

//Una enumeración de transporte
enum Transporte{
    COCHE, CAMION, AVION, TREN, BARCO;
}

class Enumerados {
    public static void main(String[] args) {
        Transporte tp;
        tp=Transporte.AVION;

        System.out.println("Valor de tp: "+tp +"\n");
        System.out.println();

        tp=Transporte.TREN;

        //Comparación de 2 valores enum
        if (tp==Transporte.TREN)
            System.out.println("tp tiene el valor de TREN\n");

        //enum para controlar sentencia switch
        switch(tp){
            case COCHE:
                System.out.println("Un auto lleva personas.");
                break;
            case CAMION:
                System.out.println("Un camión lleva carga.");
                break;
            case AVION:
                System.out.println("Un avión vuela.");
                break;
            case TREN:
                System.out.println("Un tren corre sobre rieles.");
                 break;
            case BARCO:
                System.out.println("Un barco navega en el agua.");
                break;
        }
    }
}