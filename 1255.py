for i in range(N):
    # Cria e inicializa o vetor contador
    contador = [0]*26
    # Lê o texto deste caso de teste
    texto = input()
    
    # Percorre cada caracter do texto e o
    # converte para minúsculo, e verifica
    # se está no intervalo ASCII de 97 (a)
    # a 122 (z).
    # Se estiver então subtrai de 97 para indexar
    # corretamente o vetor contador
    for j in range(len(texto)):
        minus = ord(texto[j].lower())
        if minus >= 97 and minus <= 122:
            contador[minus - 97] += 1
    
    # Encontra a letra de maior frequência
    maiorfreq = -1
    for j in range(26):
        if contador[j] > maiorfreq:
            maiorfreq = contador[j]
        
    # Percorre o vetor contador e mostra todas
    # as letras que possuem a mesma maior frequência
    for j in range(26):
        if (contador[j] == maiorfreq):
            print(chr(j+97), end="")
    print() # Pular de linha para atender o requisito de saída