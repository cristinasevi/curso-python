# Escribe un programa que pida dos números y que muestre cuál es el menor y cuál el mayor o que escriba que son iguales.

numero1 = int(input("Escribe un número: "))
numero2 = int(input("EScribe otro número: "))

if numero1 > numero2:
    print("El número", numero1, "es mayor que ", numero2)
else:
    print("El número", numero2, "es mayor que", numero1)

if numero1 == numero2:
    print("Los números son iguales")
