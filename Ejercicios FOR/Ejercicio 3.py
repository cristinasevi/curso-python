# Escribe un programa que pregunte cuántos números se van a introducir, solicite esos números y escriba cuántos número negativos se han introducido.

numeros = int(input("¿Cuántos números vas a introducir?: "))

contador = int(0)
for i in range(1, numeros + 1):
    numero1 = float(input("Escriba un número: "))
    if numero1 < 0:
        contador = contador + 1
    if contador == 0:
        print("No ha escrito ningún número negativo.")
    elif contador == 1:
        print("Ha escrito 1 número negativo.")
    else:
        print("En total ha escrito", contador, "números negativos.")
