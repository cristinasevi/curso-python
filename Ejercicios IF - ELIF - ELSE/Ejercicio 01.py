# Escribe un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.

par = input("Escribe un número par: ")
impar = input("Escribe un número impar: ")
par = int(par)
impar = int(impar)

if par % 2 == 0 and impar % 2 > 0:
    print("Los números son correctos")
else:
    print("Uno o más números no son correctos")
