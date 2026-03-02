 # Programa para contar palabras en un archivo de texto
 
# 1. Pedir al usuario la ruta de un archivo de texto.

# 2. Leer el contenido del archivo.

# 3. Separar en palabras.

# 4. Contar número total de palabras.

# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

import re
from collections import Counter

archivo = input("Ingrese la ruta del archivo: ")
try:
    with open(archivo, 'r',encoding='utf-8') as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe.")
    exit()


palabras = re.findall(r'\b\w+\b', contenido.lower())
total_palabras = len(palabras)

print(f"El archivo tiene {total_palabras} palabras.")

contador = Counter(palabras)
mas_comunes = contador.most_common(10)

print("\nLas 10 palabras más frecuentes:")
for palabra, conteo in mas_comunes:
    print(f"{palabra}: {conteo}")
