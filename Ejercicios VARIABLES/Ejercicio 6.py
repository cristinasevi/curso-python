# Escribe un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius.

# Se recuerda que la relación entre grados Celsius (ºC) y grados Fahrenheit (ºF) es la siguiente: C = (F - 32) / 1,8
fahrenheit = float(input("Escribe una temperatura en ºF: "))

celsius = float(round((fahrenheit - 32)/1.8, 3))
print("Su temperatura es de:", celsius, "ºC")
