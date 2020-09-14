#VITORIA ROCHA
f=[]
b=[]
#variavel contadora
cont=0
n=int(input())
visitas=2*n
#lendo especies
for i in range(n):
    l=[]
    for j in range(n):
        l+=[0]
    f+=[l]
    
#lendo celulas
for i in range(n):
    linha = input().split()
    for j in range(n):
        f[i][j]=int(l[j])
b = [0]*visitas
for i in range(1,visitas):
    x,y = input().split()
    
    if f[int(x)-1][int(y)-1] != b[i - 1]:
        cont+=1
        b[i - 1] += f[int(x)-1][int(y)-1]
        
#mostrando pro usuario
print(cont)