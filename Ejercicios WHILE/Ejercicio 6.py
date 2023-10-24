# Escribe un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario tiene que adivinarlo). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y después el usuario va probando valores y el programa va diciendo si son demasiado grandes o pequeños.

import random

intentosrealizados = 0

número = random.randint(1, 20)
print("Adivina el número que estoy pensando entre el 0 y el 100")

while intentosrealizados < 6:
    print("Intenta adivinar")
    estimación = input()
    estimación = int(estimación)
    intentosrealizados = intentosrealizados + 1

    if estimación < número:
        print("Prueba con un número más alto")
    if estimación > número:
        print("Prueba con un número más bajo")

    if estimación == número:
        break
if estimación == número:
    intentosrealizados = str(intentosrealizados)
    print("Lo has adivinado, en", intentosrealizados, "intentos!")
if estimación != número:
    número = str(número)
    print("El número que estaba pensando era", número)
