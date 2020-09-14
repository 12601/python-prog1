import matrizes.py
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for n in range (0,3):
    for m in range (0,3):
        matriz[n][m] = int(input())

for n in range (0,3):
    for m in range (0,3):
        print(f'[{matriz[n][m]:^5}]', end='')
    print()