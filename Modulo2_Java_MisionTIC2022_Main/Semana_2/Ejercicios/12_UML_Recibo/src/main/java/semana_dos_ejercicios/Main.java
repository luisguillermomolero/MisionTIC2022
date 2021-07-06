package semana_dos_ejercicios;

public class Main {
    
    public static void main(String[] args){
        Recibo recibo = new Recibo(27, 10, 2011, "DeNada. S.A", 2023);

        recibo.setTipo("R");
        recibo.setNumero(1);
        recibo.setDetalle("Pago servicios mensajeria");
        recibo.setTotal(5000);
        recibo.Mostrar();


    }
}
