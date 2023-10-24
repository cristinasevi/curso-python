# Escribe un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son.
# Recuerda que una gruesa son 12 docenas.

cantidad = int(input("Escribe una cantidad: "))

resultado_gruesa = int
resultado_docenas = int
resultado_unidades = int
resultado_gruesa = (cantidad // 144)
resultado_docenas = ((cantidad % 144)//12)
resultado_unidades = ((cantidad % 144) % 12)
print("Su cantidad es:", resultado_gruesa, "gruesa", resultado_docenas, "docenas", resultado_unidades, "unidades")
