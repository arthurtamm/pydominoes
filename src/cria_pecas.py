from random import shuffle
def cria_pecas():
    pecas = [] 
    for i in range(0,7):
        for k in range(i,7):
            pecas.append([i,k])
    shuffle(pecas)
    return pecas



    