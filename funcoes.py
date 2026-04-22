import random

def rolar_dados(n):

    lista = []

    i = 0
    while i < n:
        numero = random.randint(1, 6)
        lista.append(numero)
        i += 1
    
    return lista
