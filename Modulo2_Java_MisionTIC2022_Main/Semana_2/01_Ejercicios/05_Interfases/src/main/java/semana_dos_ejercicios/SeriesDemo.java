package semana_dos_ejercicios;

class SeriesDemo {
    public static void main(String[] args) {
        DeDos ob = new DeDos();

        for (int i=0;i<3;i++)
            System.out.println("Siguiente valor es: "+ob.getSiguiente());
            System.out.println("El valor anterior a " + ob.getSiguiente() + " es " + ob.getAnterior());

        System.out.println("\nReiniciando");
        ob.reiniciar();
        for (int i=0;i<3;i++)
            System.out.println("Siguiente valor es: "+ob.getSiguiente());
            System.out.println("El valor anterior a " + ob.getSiguiente() + " es " + ob.getAnterior());
            System.out.println("\nIniciando en 100");
            
        ob.setComenzar(100);
        for (int i=0;i<3;i++)
            System.out.println("Siguiente valor es: "+ob.getSiguiente());
            System.out.println("El valor anterior a " + ob.getSiguiente() + " es " + ob.getAnterior());
    }
}