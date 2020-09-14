cont = 0
media = 0
while(cont < 2):
    nota = float(input())
    if (nota>= 0 and nota<=10):
        media = nota + media
        cont = cont + 1
    else:
        print('nota invalida')
media = media/cont
print('media = %.2f'%media)