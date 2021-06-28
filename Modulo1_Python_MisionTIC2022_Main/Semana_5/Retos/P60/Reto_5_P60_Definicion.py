import pandas as pd

#ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022/blob/3f3847bbf2dbe4b2cf4dcceb96a455d92c88f9c5/movies.csv?raw=true' 

def listaPeliculas(rutaFileCsv: str)-> str:
    if rutaFileCsv.split('.')[-1] != 'csv': 
        try:
            csv = pd.read_csv(rutaFileCsv)
            #print(csv)

            #Se lee e importa un subconjunto de columnas desde la 1 hasta la 7
            subconjuntoColumnas = pd.read_csv(rutaFileCsv, usecols = [1, 2, 3, 4, 5, 6, 7])
            #Se muestra el subconjunto de películas [1338 rows x 7 columns]
            #print(subconjuntoColumnas)

            #se resta el presupuesto de las ganancias brutas para obtener las "Net Earnings".
            csv["Net Earnings"] = csv["Gross Earnings"] - csv["Budget"]

            #se ordenan los datos por la columna "Net Earnings
            ordenarPeliculas = csv[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
            #Se muestra la columna 'Net Earnings'
            print(ordenarPeliculas)


            #Se importa la libreria matplotlib.pyplot
            #import matplotlib.pyplot as plt
            #ordenarPeliculas.head(10)['Net Earnings'].plot(kind="pie")
            #Se muestra el resultado con un diagrama tipo pie de los primeros 10 registros.
            #plt.show()
        except:  
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')
    return
print(listaPeliculas(rutaFileCsv))
