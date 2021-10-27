def posicoes_possiveis(mesa, pecas):
    if len(mesa) == 0:
        return list(range(0, len(pecas)))

    exit = []
    for i in range(0, len(pecas)):
        if mesa[0][0] in pecas[i] or mesa[-1][-1] in pecas[i]:
            exit.append(i)
    return exit
