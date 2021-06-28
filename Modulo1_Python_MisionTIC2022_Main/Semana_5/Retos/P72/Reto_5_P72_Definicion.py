import pandas as pd

#ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022/blob/3f3847bbf2dbe4b2cf4dcceb96a455d92c88f9c5/movies.csv?raw=true' 

def listaPeliculas(rutaFileCsv: str)-> str:
    if rutaFileCsv.split('.')[-1] != 'csv': 
        try:
            csv = pd.read_csv(rutaFileCsv)
            #print(csv)

            #Se selecciona la columna 'Year' como indice y la columna 'Gross Earnings' para aplicar la fórmula de resumen
            subGrupoPeliculas = csv[['Year', 'Gross Earnings']]
            #print(subGrupoPeliculas)
            #Con pivot_table indexamos 'Year'
            gananciaAno = subGrupoPeliculas.pivot_table(index=['Year'])
            print(gananciaAno.head(10))
            #Se importa la libreria matplotlib.pyplot
            #import matplotlib.pyplot as plt
            #gananciaAno.plot()
            #Se muestra la columna 'Net Earnings' [76 rows x 1 columns]
            #print('\n Ganancia por Año')
            #Se muestra el resultado con la grafica
            #plt.show()
        except:  
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')
    return
print(listaPeliculas(rutaFileCsv))
