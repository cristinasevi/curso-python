# Escribe un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (imc).

# Se recuerda que el imc se calcula con la fórmula imc = peso / altura^2
peso = float(input("Introduzca su peso en kilogramos: "))
altura = float(input("Introduzca su altura en metros: "))

imc = (peso / (altura)**2)
print("Su IMC es:", imc)
