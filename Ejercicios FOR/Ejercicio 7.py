# Escribe un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética.
# Recuerde que la media aritmética de un conjunto de valores es la suma de esos valores dividida por la cantidad de valores.


numero = int(input("¿Cuántos números vas a introducir?: "))

if numero <= 0:
    print("Inténtelo de nuevo")
else:
    valor = float(input("Escribe el número 1: "))
    minimo = maximo = suma = valor
    for i in range(2, numero + 1):
        valor = float(input(f"Escribe el número {i}: "))
        suma = suma + valor
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor
    print(f"El número menor de los introducidos es {minimo}")
    print(f"El número mayor de los introducidos es {maximo}")
    print(
        f"La media aritmética de los números introducidos es {suma / numero}")
