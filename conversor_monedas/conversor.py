pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_Dolar = 3875
dolares = pesos / valor_Dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")