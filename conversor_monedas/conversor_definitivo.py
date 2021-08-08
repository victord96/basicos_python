def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos) 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """Bienvenido al conversor de monedas 💰
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

eleccion = int(input(menu))

if eleccion == 1:
    conversor("colombianos", 3875)
elif eleccion == 2:
    conversor("argentinos", 65)
elif eleccion == 3:
    conversor("mexicanos", 24)   
else:
    print("Introduce una opción correcta")    