# Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
# Recuerda que un pie son 12 pulgadas y una pulgada son 2,54 cm.

pies = float(input("Escribe una distancia en pies: "))

resultado = float(pies * 12 * 2.54)
print("Su distancia es de:", resultado, "cm")
