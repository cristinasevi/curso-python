# Escribe un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
# Recuerda que un pie son 12 pulgadas y una pulgada son 2,54 cm.

pulgadas = float(input("Escribe una distancia en pulgadas: "))

resultado = float((pulgadas * 2.54))
print("Su distancia es de:", resultado, "cm")
