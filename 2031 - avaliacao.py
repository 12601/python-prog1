x = int(input())
while(x>0):
    jogador1 = input()
    jogador2 = input()

    if((jogador1 == 'ataque' and jogador2 == 'pedra') or (jogador2 == 'ataque' and jogador1 == 'pedra')):
        if(jogador1 == 'ataque'):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")

    if((jogador1 == 'ataque' and jogador2 == 'papel') or (jogador2 == 'ataque' and jogador1 == 'papel')):
        if(jogador1 == 'ataque'):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
        
    if((jogador1 == 'pedra' and jogador2 == 'papel') or (jogador2 == 'pedra' and jogador1 == 'papel')):
        if(jogador1 == 'pedra'):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
            
    if(jogador1 == 'papel' and jogador2 == 'papel'):
        print("Ambos venceram")
        
    if(jogador1 == 'ataque' and jogador2 == 'ataque'):
        print("Aniquilacao mutua")

    if(jogador1 == 'pedra' and jogador2 == 'pedra'):
        print("Sem ganhador")
    
    x = x-1