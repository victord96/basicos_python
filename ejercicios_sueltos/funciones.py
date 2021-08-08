# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(mensaje):
    print("Hola")
    print("Cómo estas")
    print("Elegiste la opción " + mensaje)
    print("Adios")

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    conversacion("1")
elif opcion == 2:
    conversacion("2")  
elif opcion == 3:
    conversacion("3") 
else:
    print("Escribe la opción correcta")      