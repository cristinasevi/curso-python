# Escribe un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros situados entre ellos. El programa finaliza cuando se escriba un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la cantidad de números escritos.

mínimo = int(input("Escribe un número: "))
máximo = int(input("Escribe un número mayor que %d:" % mínimo))
while mínimo >= máximo:
    máximo = int(
        input(" %d no es mayor que %d . Inténtalo de nuevo: " % (máximo, mínimo)))

print()
número = float(input("Escribe un número entre %d y %d :" % (mínimo, máximo)))
contador = 0

while mínimo <= numero and numero <= máximo:
    contador += 1
    numero = float(input("Escribe otro número entre %d y %d :" %
                   (mínimo, máximo)))

print()
if contador == 0:
    print("No has escrito ningún número entre %d y %d :" % (mínimo, máximo))
elif contador == 1:
    print("Has escrito 1 número entre %d y %d :" % (mínimo, máximo))
else:
    print("Has escrito", contador, "números entre %d y %d." % (mínimo, máximo))
