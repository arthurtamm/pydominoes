def soma_pecas(pecas):
    soma = 0
    if len(pecas) == 0:
        return 0
    for i in pecas:
        soma += i[0] + i[1]
    return soma
