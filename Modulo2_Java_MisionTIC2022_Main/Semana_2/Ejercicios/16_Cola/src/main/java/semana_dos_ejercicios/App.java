/**Colas en Java con Queue: En Java podemos encontrar variadas formas de crear Colas, un ejemplo, es una de sus Interfaces que tiene como nombre “Queue”.  Los métodos de Queue para manejo de Colas en Java son los siguientes:

Para Insertar:
– add(e)
– offer(e)

Para Extraer:
– remove()
– poll()

Para Consultar el Frente:
– element()
– peek()
 */

package semana_dos_ejercicios;

import java.util.LinkedList;
import java.util.Queue;
 
public class App {    
    public static void main(String[] args) {
        /*Creamos la Cola Indicando el tipo de dato*/
        Queue<Integer> cola=new LinkedList();
        /*Insertamos datos*/
            cola.offer(3); //insertar un elemento (mejor método)
            cola.add(14);  //insertar otro elemento (lanza excepciones)
            cola.offer(12);
            cola.add(7);
            cola.offer(10);
        /*Impresion de la Cola llena con los datos*/
        System.out.println("Cola llena: " + cola);
        /*Estructura repetitiva para desencolar*/
        while(cola.poll()!=null){//Recuperar el primer elemento, si es null=vacia
            System.out.println(cola.peek());//Muestra el primer elemento de la cola
        }
        /*Muestra null debido a que la cola ya esta vacia*/
        System.out.println(cola.peek());     
    }
}