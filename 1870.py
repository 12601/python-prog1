while True:
    string = input().split()
    L = int(string[0])
    C = int(string[1])
    P = int(string[2])
    if (L == 0 and C == 0 and P == 0):
        break

    # A seguir está a construção da matriz de L linhas e C colunas
    caixa = [] # lista vazia
    for i in range(L):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(C): # Cria uma linha que é uma lista com m colunas
            linha = linha + [0] # Cada posição tem o valor 0	
        # coloque linha na matriz
        caixa += [linha]
    
    # A seguir está a leitura da matriz
    for i in range(L):
        linha = input().split() # Lê os C valores da linha
        for j in range(C): 
            caixa[i][j] = int(linha[j]) # Atribui os C valores na matriz

    balao = P - 1 # Ajustar para a coluna em Python
    
    # A seguir está a trajetória do balão
    i = 0         # Inicia na linha 0
    boom = False  # Utilizado para verificar se houve estouro do balão
    # No laço a seguir, enquanto não houver estouro se vai até a linha L-1
    while not boom and i <= L - 1:
        # O laço a seguir verifica qual é o próximo ventilador à esquerda
        # da coluna do balão, guardando a coluna e a potência
        for j in range (balao, -1, -1):
            if (caixa[i][j] > 0):
                ventEsq = j
                potEsq = caixa[i][j]
                break
            
        # O laço a seguir verifica qual é o próximo ventilador à direita
        # da coluna do balão, guardando a coluna e a potência
        for k in range (balao, C):
            if (caixa[i][k] > 0):
                ventDir = k
                potDir = caixa[i][k]
                break

        # Diferença entre as potências dos ventiladores encontrados
        dif = potEsq - potDir 
        if dif < 0: # Os cálculos a seguir são com dif negativo
            # O teste a seguir verifica se o deslocamento irá
            # passar pelo ventilador à esquerda mais próximo
            if (balao + dif <= ventEsq):
                boom = True
                balao = ventEsq
            else:
                balao = balao + dif
        elif dif > 0: # Os cálculos a seguir são com dif positivo
            # O teste a seguir verifica se o deslocamento irá
            # passar pelo ventilador à direita mais próximo            
            if (balao + dif >= ventDir):
                boom = True
                balao = ventDir
            else:
                balao = balao + dif    
        i = i + 1 # Prepara para ir à próxima linha
    # Nos casos a seguir, deve-se incrementar de 1 a coluna para que
    # seja ajustada de acordo com o enunciado: L, C e P (1 ≤ L ≤ C ≤ P ≤ 9)
    if boom == True: # Se houve estouro do balão
        # A linha já foi incrementada de 1 antes de sair do laço while
        print("BOOM", str(i), str(balao+1))
    else:            # Caso contrário mostra somente a coluna
        print("OUT", str(balao+1))