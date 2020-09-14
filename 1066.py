a = input()
b = input()
c = input()
d = input()
e = input()

a,b,c,d,e = int(a), int(b), int(c), int(d), int(e)

par = 0
impar = 0
positivo = 0
negativo = 0

if(a%2==0):
    par+=1
else:
    impar+=1
if(b%2==0):
    par+=1
else:
    impar+=1
if(c%2==0):
    par+=1
else:
    impar+=1
if(d%2==0):
    par+=1
else:
    impar+=1
if(e%2==0):
    par+=1
else:
    impar+=1
    
if(a>0):
    positivo+=1
else:
    if(a!=0):
        negativo+=1
if(b>0):
    positivo+=1
else:
    if(b!=0):
        negativo+=1
if(c>0):
    positivo+=1
else:
    if(c!=0):
        negativo+=1
if(d>0):
    positivo+=1
else:
    if(d!=0):
        negativo+=1
if(e>0):
    positivo+=1
else:
    if(e!=0):
        negativo+=1
    
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(positivo, 'valor(es) positivo(s)')
print(negativo, 'valor(es) negativo(s)')
