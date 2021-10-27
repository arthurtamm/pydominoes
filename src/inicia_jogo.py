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
            
            