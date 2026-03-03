# Contador de palabras

Pequeño script en Python que cuenta cuántas palabras hay en un archivo de texto usando expresiones regulares.

## Uso

1. Colocar el texto en `contar.txt`.
2. Ejecutar:

python contador.py

# calculadora.py

Calculadora de operaciones basicas, que repite su proposito hasta que se indique por el usuario "salir".

## Uso

Ejecutar el script con:

python calculadora.py

Luego, sigue las instrucciones que aparecen en pantalla: podrás elegir entre sumar, restar, multiplicar o dividir dos números. Cuando quieras salir, escribe "salir" cuando se te pregunte la operación.

# fizzbuzz.py

Clásico script de programación, realizado con una pequeña diferencia donde se le solicita al usuario ingresar un número entre 1 a 200. El resto del programa funciona de igual manera, se imprimirá Fizz a los números divisibles por 3, Buzz a los divisibles por 5 y FizzBuzz a los divisibles por 3 y 5. El resto de números se imprimiran normalmente.

## Uso

Ejecutar el script con:

python fizzbuzz.py

Seguir instrucciones en pantalla.

# analisis_datos.py

Script para análisis de datos en archivos CSV. 
- El programa solicita al usuario la ruta de un archivo CSV (soporta archivos con 2 o 3 columnas de datos numéricos).
- Calcula y muestra estadísticas básicas (media, mediana, moda, desviación estándar) de las columnas numéricas principales.
- Si el CSV tiene 3 columnas, la primera se usa como eje X, y se muestran/gráfican las otras dos.
- Si el CSV tiene 2 columnas, calcula las estadísticas de ambas y grafica los valores en función de su posición (índice de fila).
- Presenta una gráfica de dispersión comparando los datos numéricos. 
- Informa al usuario en caso de error de lectura del archivo.

## Uso

Para usar este script, asegúrate de tener instalado Python y las librerías `pandas` y `matplotlib`. 
Al ejecutarlo, el programa te pedirá que ingreses la ruta del archivo CSV que deseas analizar (por ejemplo: `2_columnas.csv` o `3_columnas.csv`).

Sigue estos pasos:

1. Prepara tu archivo CSV con 2 o 3 columnas de datos numéricos (puedes usar los archivos de ejemplo incluidos).
2. Ejecuta el script:

   python analisis_datos.py

3. Cuando se te pida, escribe la ruta del archivo CSV.
4. El programa mostrará estadísticas descriptivas básicas de las columnas y generará una gráfica de dispersión.
5. Si ocurre algún error, el script te avisará y podrás intentar de nuevo.

## Aprendizaje

Estos programas se realizaron aprendiendo a utilizar Cursor en programacion.