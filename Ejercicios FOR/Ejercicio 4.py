# Escribe un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre al final cuántos han sido pares y cuántos impares.

numeros = int(input("¿Cuántos números vas a introducir?: "))
contador_impar = int(0)
contador_par = int(0)

for i in range(numeros):
    numero1 = int(input("Escribe un número: "))
    if numero1 % 2 == 0:
        contador_par = contador_par + 1
    else:
        contador_impar = contador_impar + 1

print(contador_impar, "números impares", contador_par, "números pares")
