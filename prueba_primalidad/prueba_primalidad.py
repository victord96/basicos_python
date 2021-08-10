# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False            


# def run():
#     numero = int(input("Escribe un número: "))
#     if es_primo(numero):
#         print("Es primo")
#     else:
#         print("No es primo")     


# if __name__ == "__main__":
#     run()


#Para saber si un número es primo o compuesto basta con dividirlo por los números primos menores que él hasta llegar a un cociente igual o menor que el divisor.


import sys


# #Con esta función averiguamos si vamos a utilizar o no un número como divisor, en función de si es primo o no
def es_divisor(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False  


# #Con esta función sabremos si el numero es primo o no
def es_primo(dividendo, divisor):
    if dividendo % divisor == 0:
        return False
    else:
        return True    


def run():
    numero = int(input("Escribe un número: "))
    i = 2

    if numero == 1:
        print("No es primo")

    while i < numero:
        if es_divisor(i):
            if es_primo(numero, i):
                i += 1 
            else:
                print("No es primo")
                sys.exit()
        else:
            i += 1        
    print("Es primo")

if __name__ == "__main__":
    run()  
