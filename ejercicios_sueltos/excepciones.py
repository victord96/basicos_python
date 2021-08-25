def run():
    def divide_elementos_De_listas(lista, divisor):
        try:    
            return [i / divisor for i in lista]
        except ZeroDivisionError as e:
            print(e)
            return lista

    lista = list(range(10))
    divisor = 0

    print(divide_elementos_De_listas(lista, divisor))    


if __name__ == '__main__':
    run()