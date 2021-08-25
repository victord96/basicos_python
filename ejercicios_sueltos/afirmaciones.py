import random

def adivina_el_numero(n):
        num_ganador = random.randint
        if n == num_ganador:
            print("Acertaste, felicitaciones")
        else:
            print('Ingrese otro numero')    

def run():
    n = input('Por favor, introduce un numero: ')
    assert type(n) == int, f'{n} no es int'
    adivina_el_numero(n)


if __name__ == '__main__':
    run()