def verifica_ganhador(hands):
    for player, hand in hands.items():
        if len(hand) == 0:
            return player
    return -1
    
    
