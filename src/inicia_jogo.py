def inicia_jogo(j,pecas):
    game = {}
    game['jogadores'] = {}
    game['monte'] = []
    game['mesa'] = []
    for i in range(0,j):
        game['jogadores'][i] = []

    for i in range(0,8):
        game['jogadores'][i].append(pecas[i])
            
            