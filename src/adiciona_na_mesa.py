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