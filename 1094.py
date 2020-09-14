n = int(input())
x = 0
x = int(x)
total = 0
contc = 0
contr = 0
conts = 0

while(n>0 and n<=15):
    x, y = input().split()
    
    if(y == "C"): #Coelhos
        contc = contc + x
        
    if(y == "R"): #Ratos
        contr = contr + x
        
    if(y == "S"): #Sapos
        conts = conts + x
    n = n-1
    
total = contc + contr + conts

pc = (contc*100)/total
pr = (contr*100)/total
ps = (conts*100)/total

print('Total:',total, 'cobaias')
print('Total de coelhos:',contc)
print('Total de ratos:',contr)
print('Total de sapos:',conts)
print('Percentual de coelhos: %.2f'%pc,'%')
print('Percentual de ratos: %.2f'%pr,'%')
print('Percentual de sapos: %.2f'%ps,'%')