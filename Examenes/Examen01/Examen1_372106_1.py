"""
Se le solicita al usuario ingresar 3 valores(números enteros o de punto flotante) y desplegar como resultado lo siguiente:

    1. Mostrar si los tres valores son iguales o no.
    2. Mostrar los números en orden descendente. También debe funcionar para números duplicados.
    3. Solo podrá utilizar los operadores, sentencia if(anidada), símbolos y funciones vistos en clase.
    4. El resultado de salida debe ser idéntico al mencionado en este examen.
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Igualdad
if num1 == num2:
    if num2 == num3:
        print(f"Los valores {num3}, {num2} y {num1} son iguales.")
        print(f"Todos los numeros son iguales, por lo tanto no es necesario mostrar su ordenamiento.")

if min(num1, num2, num3) != max(num1, num2, num3):
    print(f"Los valores {num1}, {num2} y {num3} no son iguales.")
    # Orden descendente
    if num1 > num2:
        if num2 > num3:
            print(f"El orden de los números de forma descendente son: {num1}, {num2} y {num3}.")
        if num2 <= num3:
            if num1 > num3:
                print(f"El orden de los números de forma descendente son: {num1}, {num3} y {num2}.")
            if num1 <= num3:
                print(f"El orden de los números de forma descendente son: {num3}, {num1} y {num2}.")

    if num1 <= num2:
        if num1 > num3:
            print(f"El orden de los números de forma descendente son: {num2}, {num1} y {num3}.")
        if num1 <= num3:
            if num2 > num3:
                print(f"El orden de los números de forma descendente son: {num2}, {num3} y {num1}.")
            if num2 <= num3:
                print(f"El orden de los números de forma descendente son: {num3}, {num2} y {num1}.")