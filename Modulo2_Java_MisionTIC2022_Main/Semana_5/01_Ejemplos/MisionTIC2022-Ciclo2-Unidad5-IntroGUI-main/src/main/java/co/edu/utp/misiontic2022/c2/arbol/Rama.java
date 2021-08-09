package co.edu.utp.misiontic2022.c2.arbol;

import javax.swing.tree.DefaultMutableTreeNode;

public class Rama {
    DefaultMutableTreeNode r;

    public Rama(String datos[]) {
        r = new DefaultMutableTreeNode(datos[0]);
        for (int i = 1; i < datos.length; i++)
            r.add(new DefaultMutableTreeNode(datos[i]));
    }

    public DefaultMutableTreeNode node() {
        return (r);
    }
}
