# Escribe un programa que pida primero un número par y a continuación un numero impar (positivos o negativos). En caso de que uno o los dos valores no sean correctos, se mostrarán uno o dos avisos.

par = int(input("Escribe un número par: "))
impar = int(input("Escribe un número impar: "))

if par % 2 == 1:
    print("No has escrito un número par.")

if impar % 2 == 0:
    print("No has escrito un número impar.")
