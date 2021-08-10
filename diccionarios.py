def run():
    # mi_diccionario = {
    #     "llave1": 1,
    #     "llave2": 2,
    #     "llave3": 3,
    # }
    
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina": 4532764,
        "Brasil": 6237238346,
        "Colombia": 6386432
    }

    #print(poblacion_paises["Argentina"])
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais, poblacion in poblacion_paises.items():
    #     print(pais + " tiene " + str(poblacion) + " habitantes")


divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

opcion = int(input("""¿Cual escoges? 
1. Euro 
2. Dolar
3. Yen 
"""))

if opcion == 1:
    print(divisas["Euro"])
elif opcion == 2:
    print(divisas["Dollar"])
elif opcion == 3:
    print(divisas["Yen"])  
else:
    print("Introduce una opcion correcta")     

if __name__ == "__main__":
    run()