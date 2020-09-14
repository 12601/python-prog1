i = 1
total = 0
sinal = []

while True:
    x = input()
    expressao = x.replace('+', ' ').replace('-', ' ').split()

    # Transformando os valores em inteiro:
    for m in range(len(expressao)):
        expressao[m] = int(expressao[m])

    # Pegando os sinais na ordem:
    for i in range(len(x)):
        if x[i] == '+':
            sinal.append('+')
        elif x[i] == '-':
            sinal.append('-')

    # Iniciando a variavel:
    total = expressao[0]

    # Realizando as operações:
    k = 0
    while k < len(sinal):
        if sinal[k] == '+':
            total += expressao[k+1]
        elif sinal[k] == '-':
            total -= expressao[k+1]
        k = k + 1

    # Printando e resetando as variavies:
    print('Teste', j)
    print(total, '\n')
    j += 1
    expressao = []
    sinal = []