#Redução de condicionais
sinal1 = bool(input())
sinal2 = bool(input())
sinal3 = bool(input())
sinal4 = bool(input())

if[(sinal1 or sinal2) and (sinal3 or sinal1) and (sinal4 or not not sinal1)] and [(sinal2 and sinal3 and sinal4) or not sinal1]:
    print('liberado')
else:
    print('nao liberado')

if[(sinal1 or sinal2) and (sinal3 or sinal1) and (sinal4 or sinal1)] and [(sinal2 and sinal3 and sinal4) or not sinal1]:
    print('liberado')
else:
    print('nao liberado')
