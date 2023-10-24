# Escribe un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe un número: "))
numero3 = int(input("Escribe un número: "))

if numero1 == numero2 == numero3:
    print("Los tres números son iguales")
else:
    if numero1 != numero2 and numero2 != numero3 and numero1 != numero3:
        print("Los números son diferentes")
    else:
        print("Uno de esos números es diferente")
