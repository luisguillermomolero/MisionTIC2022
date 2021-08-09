package semana_dos_ejercicios;

import java.util.HashMap;

public class App {
  public static void main(String[] args) {

    HashMap<Integer, String> m = new HashMap<>();

    m.put(924, "Amalia Núñez");
    m.put(921, "Cindy Nero");
    m.put(700, "César Vázquez");
    m.put(219, "Víctor Tilla");
    m.put(537, "Alan Brito");
    m.put(605, "Esteban Quito ");

    System.out.println(m.get(921));
    System.out.println(m.get(605));
    System.out.println(m.get(888)); 
  }
}