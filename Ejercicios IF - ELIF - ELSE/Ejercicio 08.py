# Escribe un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

fecha1 = int(input("Escribe el año actual: "))
fecha2 = int(input("Escribe un año cualquiera: "))

if fecha1 > fecha2:
    print("Desde el año", fecha2, "han pasado", (fecha1-fecha2), "años.")
elif fecha1 < fecha2:
    print("Para llegar al año", fecha2, "faltan", (fecha2 - fecha1), "años.")
else:
    print("¡Son el mismo año!")
