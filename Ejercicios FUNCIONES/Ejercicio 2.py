# Escribe una función que pida un año como parámetro y que escriba si es bisiesto o no.
# Recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

fecha = int(input("Escribe un año y le diré si es bisiesto: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print("El año", fecha, "es un año bisiesto")
else:
    print("El año", fecha, "no es un año bisiesto")
