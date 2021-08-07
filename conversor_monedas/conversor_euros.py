valor_cambio = 0.85
eleccion = input("""Elige una opción:
1. Conversor de euros a dolares
2. Conversor de dolares a euros
""")
eleccion = int(eleccion)
if eleccion == 1:
    euros = input("""Introduce la cantidad de euros que quieres convertir: 
""")
    dolares = float(euros) / valor_cambio
    dolares = round(dolares,2)
    print("Tienes $" + str(dolares))
elif eleccion == 2:
    dolares = input("""Introduce la cantidad de dolares que quieres convertir
""")
    euros = float(dolares) * valor_cambio
    print("Tienes " + str(euros) + " €")
else:
    print("Introduce una opción correcta")    