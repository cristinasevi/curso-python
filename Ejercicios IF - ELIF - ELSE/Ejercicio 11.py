print("Elije una figura geométrica: ")
print("- Triángulo")
print("- Círculo")
respuesta = input(
    "¿Quieres calcular el área de triángulo (T) o de un círculo (C)?: ")

if respuesta == "T" or respuesta == "t":
    base = float(input("Escribe la base: "))
    altura = float(input("Escribe la altura: "))
    print(
        f"Un triángulo de base {base} y altura {altura} tiene un área de {base * altura / 2}"
    )
elif respuesta == "C" or respuesta == "c":
    r = float(input("Escribe el radio: "))
    print(f"Un círculo de radio {r} tiene un área de {3.14159 * r*r}")
