while (True):
    # Ler na mesma linha quantas temporadas (N)
    # a série tem e a duração em minutos (M) de cada capítulo.
    linha = input().split()
    N = int(linha[0])
    M = int(linha[1])
    
    if N == -1 and M == -1: # Última linha que indica término
        break
    
    # Quantos capítulos cada temporada tem.
    caps = input().split()

    # Ao mesmo tempo em que se calcula quantos minutos
    # que o casal gasta e assistir uma única temporada,
    # inclue-se a quantidade de minutos em que se
    # assiste as temporadas anteriores a cada temporada
    
    # Armazena os minutos acumulados de cada temporada
    # até a última
    acumulado = 0
    
    # Armazena o total de minutos, com o acumulado
    # até a temporada anterior mais o gasto na
    # temporada atual
    total = 0
    for i in range(N): # N temporadas
        total += acumulado + int(caps[i])*M 
        acumulado += int(caps[i])*M

        
    # Mostrar a resposta
    print(total)