# Escribe un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.

dividendo = int(input("Escribe un número entero: "))
divisor = int(input("Escribe otro número entero: "))

if dividendo % divisor == 0:
    print("La división es exacta. Cociente:", dividendo // divisor,)
else:
    print("La división no es exacta. Cociente:", dividendo // divisor, "Resto:", dividendo % divisor,)
