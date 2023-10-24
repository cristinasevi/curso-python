# Mejora el programa anterior haciendo que tenga en cuenta que no se puede dividir por cero:

dividendo = int(input("Escribe el dividendo: "))
divisor = int(input("Escribe el divisor: "))
if divisor == 0:
    print("No se puede dividir entre cero")
elif dividendo % divisor == 0:
    print("La división es exacta. Cociente:", dividendo // divisor,)
else:
    print("La división no es exacta. Cociente:", dividendo // divisor, "Resto:", dividendo % divisor,)
