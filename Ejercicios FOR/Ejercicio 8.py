# Escribe un programa que genere una multiplicación de dos números del 2 al 10 al azar, solicite el resultado y muestre si se ha dado la respuesta correcta.

import random

a = random.randrange(2, 11)
b = random.randrange(2, 11)

respuesta = int(input(f"¿Cuánto es {a} x {b}? "))

if respuesta == a * b:
    print("Correcto!")
else:
    print("Incorrecto!")
