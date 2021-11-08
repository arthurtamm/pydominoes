def adiciona_na_mesa(peca, mesa):
    inv = [peca[1], peca[0]]
   
    if len(mesa) == 0:
        return [peca]
    elif peca[0] == mesa[0][0]:
        mesa.insert(0,inv)
    elif peca[1] == mesa[0][0]:
        mesa.insert(0,peca)
    elif peca[0] == mesa[-1][-1]:
        mesa.append(peca)
    else:
        mesa.append(inv)
   
    return mesa

from random import shuffle
def cria_pecas():
    pecas = [] 
    for i in range(0,7):
        for k in range(i,7):
            pecas.append([i,k])
    shuffle(pecas)
    return pecas

def inicia_jogo(n, p):
    game = {'jogadores': {}, 'monte': [], 'mesa': []}
    k = 0
    j = 7
    for i in range(0, n):
        game['jogadores'][i] = p[k:j]
        k += 7
        j += 7
    game['monte'].extend(p[k:])
    return game

def posicoes_possiveis(mesa, pecas):
    if len(mesa) == 0:
        return list(range(0, len(pecas)))

    exit = []
    for i in range(0, len(pecas)):
        if mesa[0][0] in pecas[i] or mesa[-1][-1] in pecas[i]:
            exit.append(i)
    return exit

def soma_pecas(pecas):
    soma = 0
    if len(pecas) == 0:
        return 0
    for i in pecas:
        soma += i[0] + i[1]
    return soma

def verifica_ganhador(hands):
    for player, hand in hands.items():
        if len(hand) == 0:
            return player
    return -1
