# Escribe un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa finalizará escribiendo los dos números.

numero1 = int(input("Escribe un número entero: "))
numero2 = int(input("Escribe otro número entero: "))

while (numero1 <= numero2):
    numero2 = int(input("Escribe un número menor: "))
print("Los números que has escrito son:", numero1, "y", numero2)
