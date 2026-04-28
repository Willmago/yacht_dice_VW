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

    for i in range(len(dados_rolados)):

        if i != dado_para_guardar:
            dados_rolados_novo.append(dados_rolados[i])

    return [dados_rolados_novo, dados_no_estoque]

def remover_dado(dados_rolados,dados_no_estoque,dado_para_remover):
    dados_rolados_novo = dados_rolados
    dados_rolados_novo.append(dados_no_estoque[dado_para_remover])
    dados_estoque_novo = []

    for dado in range(len(dados_no_estoque)):
        if dado != dado_para_remover:
            dados_estoque_novo.append(dados_no_estoque[dado])

    
    return [dados_rolados_novo, dados_estoque_novo]

def  calcula_pontos_regra_simples(numeros):

    dic_pontos = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    for n in numeros:
        dic_pontos[n] += n
    
    return dic_pontos

def calcula_pontos_soma(dados):
    
    soma = 0

    for dado in dados:
        soma += dado

    return soma

def calcula_pontos_sequencia_baixa(dados):

    if 3 in dados and 4 in dados:
        if (2 in dados and 1 in dados) or (2 in dados and 5 in dados) or (5 in dados and 6 in dados):
            return 15
    
    return 0

def calcula_pontos_sequencia_alta(dados):

    if 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        if 1 in dados or 6 in dados:
            return 30
    
    return 0