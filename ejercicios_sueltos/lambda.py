def run():
    """Algunos ejercicios para practicar las funciones
       LAMBDA
    """
    suma_2 = lambda x,y : x + y
    frase = lambda str1, str2 : str1 + ' ' + str2 

    print(suma_2(4,5))
    print(frase('hola que','ase'))

if __name__ == '__main__':
    run() 