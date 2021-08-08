menu = """Bienvenido al conversor de monedas 💰
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

eleccion = int(input(menu))

if eleccion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos) 
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif eleccion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos) 
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif eleccion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos) 
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")   
else:
    print("Introduce una opción correcta")    