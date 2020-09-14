x = 0
media = 0
cont = 0

while(x >= 0):
    x = int(input())
    if(x>0):
        media = media + x
        cont = cont + 1
    elif(x==0):
        cont = cont+1
  
media = media/cont
print('%.2f'%media)