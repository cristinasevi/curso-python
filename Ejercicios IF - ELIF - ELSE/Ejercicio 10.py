# Escribe un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

print("Una ecuacion de primer grado tiene esta estructura: ax + b = 0 ")
print("La fórmula que resuelve la ecuación de primer grado es: x = -b / a")

a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))

print(a, "x +", b, "= 0")

if a == b == 0:
    print("Todos los números son solución.")
elif a == 0:
    print("La ecuación no tiene solución.")
else:
    print("La ecuación tiene una solución: X =", (- b / a))
