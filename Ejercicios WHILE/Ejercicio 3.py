# Escribe un programa que pida la cantidad de números positivos que se tienen que escribir y a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada.

numeros = int(input("¿Cuántos números positivos vas a escribir?: "))
a = int(0)
while a != numeros:
    numero1 = int(input("Escribe un número: "))
    a += 1
print("Has escrito en total", numeros, "números")
