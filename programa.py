from funcoes import *

opcoes_validas = ['0', '1', '2', '3', '4']
jogadas = 0
pontuacao = 0
cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

while jogadas < 12:

    dados_rolados = rolar_dados(5)
    dados_guardados = []

    rerrolagens = 0
    fez_jogada = False

    while fez_jogada == False:

        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')

        # Opção
        opcao = input('>')

        while opcao not in opcoes_validas:
            print("Opção inválida. Tente novamente.")
            opcao = input('>')

        match opcao:
            case '1': # Guardar
                print('Digite o índice do dado a ser guardado (0 a 4):')
                indice = int(input('>'))

                novos_dados = guardar_dado(dados_rolados, dados_guardados, indice)
                dados_rolados = novos_dados[0]
                dados_guardados = novos_dados[1]

            case '2': # Remover
                if len(dados_guardados) > 0:
                    print("Digite o índice do dado a ser removido (0 a 4):")
                    indice = int(input('>'))
                    
                    novos_dados = remover_dado(dados_rolados, dados_guardados, indice)

                    dados_rolados = novos_dados[0]
                    dados_guardados = novos_dados[1]

            case '3': # Rerrolar
                if rerrolagens < 2:
                    dados_rolados = rolar_dados(len(dados_rolados))

                    rerrolagens += 1
                else:
                    print("Você já usou todas as rerrolagens.")

            case '4': # Cartela
                imprime_cartela(cartela)

            case '0': # Jogada
                print("Digite a combinação desejada:")
                while fez_jogada == False:
                    categoria = input(">")

                    if categoria in ['1', '2', '3', '4', '5', '6']:
                        if int(categoria) in cartela['regra_simples']:
                            
                            if cartela['regra_simples'][int(categoria)] == -1:
                                dados = dados_rolados + dados_guardados
                                cartela = faz_jogada(dados, categoria, cartela)
                                fez_jogada = True
                            else:
                                print("Essa combinação já foi utilizada.")
                    elif categoria in cartela['regra_avancada']:
                        
                        if cartela['regra_avancada'][(categoria)] == -1:
                            dados = dados_rolados + dados_guardados
                            cartela = faz_jogada(dados, categoria, cartela)
                            fez_jogada = True
                        else:
                            print("Essa combinação já foi utilizada.")
                    else:
                        print("Combinação inválida. Tente novamente.")
                       

    jogadas += 1

imprime_cartela(cartela)

simples = cartela['regra_simples']
avancada = cartela['regra_avancada']

for pontos in simples.values():

    pontuacao += pontos

if pontuacao >= 63:
    pontuacao += 35

for pontos in avancada.values():

    pontuacao += pontos

print(f"Pontuação total: {pontuacao}")
