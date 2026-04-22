import random

def rolar_dados(n):

    lista = []

    i = 0
    while i < n:
        numero = random.randint(1, 6)
        lista.append(numero)
        i += 1
    
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):

    dado_que_eu_quero = dados_rolados[dado_para_guardar]

    dados_no_estoque.append(dado_que_eu_quero)

    dados_rolados_novo = []

    retirado = False
    for i in range(len(dados_rolados)):

        if i != dado_para_guardar:
            dados_rolados_novo.append(dados_rolados[i])

    return [dados_rolados_novo, dados_no_estoque]
