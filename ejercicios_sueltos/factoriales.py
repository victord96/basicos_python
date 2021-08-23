def factorial(n):
    """Calcula el factorial de n.

    Args:
        n ([int>0]): numero para calcular factorial
        [returns n!]: devuelve el factorial del numero
    """
    if n == 1:
        return 1

    return n * factorial(n-1)    

n = int(input("Escribe un entero: "))

print(factorial(n))