# Escribe un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los números introducidos supere el límite inicial.

límite = int(input("Introduzca valor limite positivo:"))
while límite <= 0:
    límite = int(input("Introduzca valor limite positivo por encima de 0:"))

print()
número = float(input("Escriba un número: "))
suma = número

while suma < límite:
    número = float(input("Escriba otro número: "))
    suma += número

print()
print("Ha superado el límite. La suma de los números introducidos es", suma)
