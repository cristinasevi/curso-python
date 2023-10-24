# Escribe un programa que pida números mientras no se escriba un número negativo. El programa finalizará escribiendo la suma de los números introducidos.

numero1 = int(input("Escribe un número negativo: "))
while numero1 > 0:
    numero1 = int(input("Escribe un número negativo: "))
else:
    numero2 = int(input("Escribe otro número negativo: "))
    while numero2 > 0:
        numero2 = int(input("Escribe un número negativo: "))
    print("El resultado de la suma es:", numero1 + numero2)
