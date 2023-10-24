# Escribe un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.

tiempo = int(input("Escribe una cantidad en segundos: "))

resultado_min = int
resultado_seg = int
resultado_min = (tiempo // 60)
resultado_seg = (tiempo % 60)
print("Su tiempo es:", resultado_min, "min", resultado_seg, "seg")
