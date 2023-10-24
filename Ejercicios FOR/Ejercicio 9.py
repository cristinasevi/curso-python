# Amplía el programa anterior haciendo que este solicite primero al usuario cuántas multiplicaciones se van a plantear.

import random

numero_multiplicaciones = int(
    input("¿Cuántas multiplicaciones quieres hacer?: "))
if numero_multiplicaciones < 1:
    print("Inténtelo de nuevo")
else:
    for _ in range(numero_multiplicaciones):
        print()
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        respuesta = int(input(f"¿Cuánto es {a} x {b}? "))

        if respuesta == a * b:
            print("Correcto!")
        else:
            print("Incorrecto!")
