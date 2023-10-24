# Escribe un programa que pida primero un número par y a continuación un numero impar (positivos o negativos). En cada petición, si el valor no es correcto se mostrará un aviso.

par = int(input("Escribe un número par: "))

if par % 2 > 0:
    print("El número no es correcto")
else:
    impar = input("Escribe un número impar: ")
    impar = int(impar)
    if impar % 2 == 0:
        print("El número no es correcto")
    else:
        print("Perfecto")
