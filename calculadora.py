#Programa para hacer operaciones basicas de una calculadora utilizando 2 numeros y repetir hasta que el usuario escriba "salir".  

#1. Pedir al usuario los 2 numeros.
#2. Pedir al usuario la operacion que desea realizar.
#3. Realizar la operacion.
#4. Mostrar el resultado.
#5. Repetir hasta que el usuario escriba "salir".

import os

while True:
    os.system('cls')
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = input("Ingrese la opción: ")
    if opcion == "5":
        break
    if not opcion.isdigit() or int(opcion) > 5 or int(opcion) < 1:
        print("Opción no valida, ingrese un numero dentro de las opciones")
        input("Presione enter para continuar...")
        continue
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if opcion == "1":
        print(f"El resultado de la suma es: {num1 + num2}")
    elif opcion == "2":
        print(f"El resultado de la resta es: {num1 - num2}")
    elif opcion == "3":
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir por 0")
        else:
            print(f"El resultado de la división es: {num1 / num2}")
    else:
        print("Opción no valida")
    input("Presione enter para continuar...")