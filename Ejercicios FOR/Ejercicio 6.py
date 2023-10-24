# Escribe un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.

numero = int(input("¿Cuántos números vas a introducir?: "))

if numero <= 0:
    print("Inténtelo de nuevo")
else:
    suma = 0
    for i in range(1, numero + 1):
        valor = float(input(f"Escribe el número {i}: "))
        suma = suma + valor
    print(f"La suma de los números introducidos es de {suma}")
