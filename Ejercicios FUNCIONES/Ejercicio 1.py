# Escribe un programa con una función rectángulo con dos parámetros (anchura y altura)  y lo dibuje con asteriscos (*)

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))

for i in range(altura):
    for j in range(anchura):
        print("*", end="")
    print()
