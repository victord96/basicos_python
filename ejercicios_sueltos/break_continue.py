def run():

    #EJERCICIOS SUELTOS

    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input("Escribe un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)



    # Algoritmo para mostrar años bisiestos que sean múltiplos de 10 en un rango dado por el usuario.

    def comprobar_bisiesto(i):     
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
              
            
    def es_multiplo(numero):
        # Si el residuo es 0, es múltiplo
        if numero % 10 == 0:
            return True
        else:
            return False         

    i = int(input("Introduce año de inicio: "))
    LIMITE = int(input("Introduce año final: "))

    while i != LIMITE+1:
        if i > 2021:
            break
        if comprobar_bisiesto(i) == True:
            if es_multiplo(i) == True:
                print (str(i) + " es un año binario y multiplo de 10" )
                i+=1
            else:
                i+=1
        else: 
            i+=1        


if __name__ == "__main__":
    run()