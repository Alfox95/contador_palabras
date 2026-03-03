# Ejercicio clásico de programación: FizzBuzz

# 1. Imprimir los números del 1 al 50.
# 2. Si el número es divisible por 3, imprimir "Fizz".
# 3. Si el número es divisible por 5, imprimir "Buzz".
# 4. Si el número es divisible por 3 y 5, imprimir "FizzBuzz".
input("Presiona Enter para iniciar FizzBuzz...")

while True:
    try:
        limite = int(input("¿Hasta qué número deseas hacer FizzBuzz? (máximo 200): "))
        if 1 <= limite <= 200:
            break
        else:
            print("Por favor, ingresa un número entre 1 y 200.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

for i in range(1, limite + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        