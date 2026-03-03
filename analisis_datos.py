# Te recomiendo un script como el siguiente para analizar un archivo CSV simple con pandas y graficar:

# Programa para analizar datos de un archivo CSV simple, de dos columnas, utilizando la libreria pandas.
# 1. Pedir al usuario la ruta del archivo CSV.
# 2. Leer el archivo CSV. Se cuenta con 2 archivos CSV, uno con 2 columnas y otro con 3 columnas.
# 3. Analizar los datos.
# 4. Calcular estadisticas basicas de las columnas.(Media, Mediana, Moda y Desviación estándar de cada columna)
# 5. Generar una gráfica de dispersión comparando las dos columnas, en caso de haber 3 columnas se tomará la primera columna como eje X y las otras dos columnas comparadas en el eje Y.
# 6. Si el archivo no existe o hay un error al leer el archivo, se debe mostrar un mensaje de error.
# 7. Se procede a cerrar el programa a través de la función exit().

import pandas as pd
import matplotlib.pyplot as plt

archivo = input("Ingresa la ruta del archivo CSV: ")

try:
    df = pd.read_csv(archivo)

    print("Primeras filas del archivo:\n", df)

    num_cols = len(df.columns)

    if num_cols == 3:
        # Primera columna se usa como eje X, NO calcular estadísticas para esta columna
        columnas_estadisticas = df.columns[1:]
        print(f"Omitiendo estadísticas para la columna de eje X: '{df.columns[0]}'")
        for columna in columnas_estadisticas:
            print(f"\nEstadísticas para la columna '{columna}':")
            print(f"Media: {df[columna].mean()}")
            print(f"Mediana: {df[columna].median()}")
            print(f"Moda: {df[columna].mode().values}")
            print(f"Desviación estándar: {df[columna].std()}")

        # Graficar las otras dos columnas usando la primera como eje X
        plt.scatter(df.iloc[:, 0], df.iloc[:, 1], label=df.columns[1])
        plt.scatter(df.iloc[:, 0], df.iloc[:, 2], label=df.columns[2])
        plt.xlabel(df.columns[0])
        plt.ylabel("Valores")
        plt.title("Gráfica de dispersión (primera columna vs otras)")
        plt.legend()
        plt.show()

        input("\nPulsa Enter para cerrar el programa...")
        exit()
    elif num_cols == 2:
        # Calcular estadisticas para ambas columnas
        for columna in df.columns:
            print(f"\nEstadísticas para la columna '{columna}':")
            print(f"Media: {df[columna].mean()}")
            print(f"Mediana: {df[columna].median()}")
            print(f"Moda: {df[columna].mode().values}")
            print(f"Desviación estándar: {df[columna].std()}")

        # Eje X es el índice/conteo de filas
        plt.scatter(df.index, df.iloc[:, 0], label=df.columns[0])
        plt.scatter(df.index, df.iloc[:, 1], label=df.columns[1])
        plt.xlabel("Índice de fila")
        plt.ylabel("Valores")
        plt.title("Gráfica de dispersión (índice vs columnas)")
        plt.legend()
        plt.show()

        input("\nPulsa Enter para cerrar el programa...")
        exit()
    else:
        print("El archivo debe tener al menos dos columnas para graficar dispersión.")
except FileNotFoundError:
    print("El archivo no existe.")
    input("\nPulsa Enter para cerrar el programa...")
    exit()
except Exception as e:
    print("Error al analizar el archivo:", e)
    input("\nPulsa Enter para cerrar el programa...")
    exit()