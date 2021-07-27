package co.edu.utp.misiontic2022.c2.cdiaz.util;

import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCUtilities {
    private static final String DATABASE_LOCATION = "sample.db";

    public static Connection getConnection() throws SQLException {
        String url = "jdbc:sqlite:" + DATABASE_LOCATION;

        return DriverManager.getConnection(url);
    }

    public static boolean isDatabaseEmpty() {
        File file = new File(DATABASE_LOCATION);
        return file.length() == 0;
    }

    public static void initDatabase(Connection connection) throws SQLException {
        
        // .Statement Provee métodos para que los desarrolladores puedan ejecutar sentencias SQL
        var statement = connection.createStatement();
        statement.execute("create table departments (id integer not null," 
                + " name varchar(50) not null," 
                + " primary key (id))");
                
        statement.execute("insert into departments values (1, 'Administrativa')");
        statement.execute("insert into departments values (2, 'Financiera')");
        statement.execute("insert into departments values (3, 'Compras')");
        statement.execute("insert into departments values (4, 'Ventas')");
        statement.execute("insert into departments values (5, 'Inventario')");
        statement.execute("insert into departments values (6, 'Manufactura')");

        statement.execute("create table employees ( id integer not null, name varchar(50) not null,"
                + " email varchar(100), department_id integer, primary key (id),"
                + " foreign key (department_id) references departments (id))");

        System.out.println("Se ha inicializado la base de datos correctamente");
    }

}
