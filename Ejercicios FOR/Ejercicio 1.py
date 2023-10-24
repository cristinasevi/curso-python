# Escribe un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

numero1 = int(input("Escribe un número entero: "))
numero2 = int(input("Escribe otro número entero: "))

for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        print("El número", i, "es par.")
    else:
        print("El número", i, "es impar.")
