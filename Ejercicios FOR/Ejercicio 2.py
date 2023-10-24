# Escribe un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

numeros = int(input("¿Cuántos números vas a introducir?: "))
numero1 = int(input("Escribe un número: "))

for i in range(numeros - 1):
    numero2 = int(input("Escribe otro número más grande que %d:" % numero1))
    if numero2 <= numero1:
        print("¡%d no es mayor que %d!" % (numero2, numero1))
