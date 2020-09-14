j = 1
total = 0
sinal = []

while int(input()) != 0:
    calc = input()
    calc2 = calc.replace('+', ' ').replace('-', ' ').split()

    # Transformando os valores em inteiro:
    for m in range(len(calc2)):
        calc2[m] = int(calc2[m])

    # Pegando os sinais na ordem:
    for i in range(len(calc)):
        if calc[i] == '+':
            sinal.append('+')
        elif calc[i] == '-':
            sinal.append('-')

    # Iniciando a variavel:
    total = calc2[0]

    # Realizando as operações:
    k = 0
    while k < len(sinal):
        if sinal[k] == '+':
            total += calc2[k+1]
        elif sinal[k] == '-':
            total -= calc2[k+1]
        k += 1

    # Printando e resetando as variavies:
    print('Teste', j)
    print(total, '\n')
    j += 1
    calc2 = []
    sinal = []
