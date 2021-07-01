//Realizado por: Mauricio Posada. Grupo P72

import java.util.Date;
import java.util.GregorianCalendar;

public class A02_Unidad_1 {

 public static void main(String[] args) {
  
  // Instanciamos 3 objetos de la clase Libro
  Libro libro_001 = new Libro("Amarte mas no pude", 85000, 2017, 04, 22);
  Libro libro_002 = new Libro("Ahogado en el código", 95000, 1995, 06, 2);
  Libro libro_003 = new Libro("Marte mi nuevo hogar", 10500, 2002, 03, 15);
  // Creamos un array
  Libro[] biblioteca = new Libro[3];
  // Asignamos los objetos en cada idice
  biblioteca[0] = libro_001;
  biblioteca[1] = libro_002;
  biblioteca[2] = libro_003;
  
  // Utilizamos un for para incrementar el iva y ejecutar los metodos
  for (Libro i: biblioteca) {
   i.setPrecioConIva(0.9);
   System.out.println("Libro 001: " + i.getNombre());
   System.out.println("Fecha de Edicion: " + i.getFecha());
   System.out.println("Valor con IVA: $" + i.getValor());
   System.out.println();
  }  

 }
 
} // creamos la clase Libro
 class Libro {
  // creamos sus atributos
  private String nombre;
  private double valor;
  private Date fecha;
  
  public Libro(String nombre, double valor, int año, int mes, int dia) {
   
   this.nombre = nombre;
   this.valor = valor;
   GregorianCalendar calendario = new GregorianCalendar(año, mes-1, dia);
   fecha = calendario.getTime();
   
  }
  // Metodo que devuelve nombre
  public String getNombre() {
   return nombre;
  }
  // metodo que devuelve valor
  public double getValor() {
   return valor;
  }
  // metodo que devuelve fecha
  public Date getFecha() {
   return fecha;
  }
  // metodo que calcula el precio con iva
  public void setPrecioConIva(double porcentaje) {
   double precioTotal = valor*porcentaje/100;
   valor += precioTotal;
  }
  
 }