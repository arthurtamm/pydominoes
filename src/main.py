import time
from random import randint

import engine


def print_resultado(game):
    jogadores = game['jogadores']

    tabela = []
    for player in range(len(jogadores)):
        pontuacao = engine.soma_pecas(jogadores[player])
        tabela.append((player, pontuacao))

    tabela.sort(key=lambda x: x[1])

    if tabela[0][0] == 0:
        print('Parabéns! Você venceu o PyDominoes!')
    else:
        print('Você perdeu! Tente sua sorte novamente!')

    mapa_posicao = {
        0: 'Primeiro',
        1: 'Segundo',
        2: 'Terceiro',
        3: 'Quarto'
    }

    for (index, player) in enumerate(tabela):
        player_num = player[0] + 1
        pontuacao = player[1]

        print('{} lugar: Jogador {} | {} pontos'.format(
            mapa_posicao[index], player_num, pontuacao))


def boas_vindas():
    print(" ")
    print("Insper Dominó")
    print("=> Design de Software")
    print("")
    print("Bem-vindo (a) ao Pydominoes! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.")
    print("")
    print("Vamos começar!")
    print("")


def main():
    boas_vindas()

    num_jogadores = int(input("Quantos jogadores? (2-4): "))
    game = engine.inicia_jogo(num_jogadores, engine.cria_pecas())

    player_rodada = randint(0, num_jogadores - 1)
    mesa = game['mesa']
    monte = game['monte']

    while engine.verifica_ganhador(game['jogadores']) == -1:
        print("MESA:")
        print(mesa)
        time.sleep(1)

        mao_player = game['jogadores'][player_rodada]
        movimentos = engine.posicoes_possiveis(mesa, mao_player)

        if (len(game['monte']) == 0 and len(movimentos) == 0):
            break

        if (len(movimentos) == 0):
            print('Sem peças disponíveis. COMPRANDO DO MONTE!')

            mao_player.append(monte[0])
            del monte[0]
        else:
            if player_rodada == 0:
                print("Jogador: Você com " + str(len(mao_player)) + " peça(s)")

                pecas_comzero = movimentos
                pecas_semzero = []
                for p in pecas_comzero:
                    pecas_semzero.append(p+1)

                print(mao_player, '\n', 'Possíveis opções: ', pecas_semzero)

                peca_escolhida = engine.escolhe_peca(pecas_semzero) - 1
                peca = mao_player[peca_escolhida]
            else:
                print("Jogador " + str(player_rodada + 1) +
                      ": com " + str(len(mao_player)) + " peças")

                pecas = mao_player
                jogadas = [pecas[x]
                           for x in engine.posicoes_possiveis(mesa, pecas)]

                peca = engine.computador(jogadas)
                peca_escolhida = pecas.index(peca)

            mesa = engine.adiciona_na_mesa(peca, mesa)
            del mao_player[peca_escolhida]
            print('Colocou:{}'.format(peca))
            print(" ")
            time.sleep(1)

        if player_rodada + 1 != num_jogadores:
            player_rodada += 1
        else:
            player_rodada = 0

    print_resultado(game)


if __name__ == "__main__":
    main()
