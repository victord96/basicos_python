import random

#Programa que genera un numero aleatorio y debes tratar de averiguar cual es el correcto entre 1 y 100
def run():
    nganador = random.randrange(100)
    ganaste = False


    n = int(input("Elige un número del 1 al 100: "))

    while ganaste == False:
        if n > 0 and n < 101:
            if n == nganador:
                print("¡Ganaste!")
                ganaste = True
                break
            else:
                if n < nganador:
                    print("Busca un número más grande")
                else:
                    print("Busca un número más pequeño")
            n = int(input("Elige otro número: "))       
        else:
            print("Por favor, introduzca un numero correcto")
            n = int(input("Elige un número del 1 al 100: "))


if __name__ == "__main__":
    run()

