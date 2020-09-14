a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if(a>=b and a>=c):
    maior = a
    if(b>=c):
        meio = b
        menor = c
    else:
        meio = c
        menor = b
        
if(b>=a and b>=c):
    maior = b
    if(a>=c):
        meio = a
        menor = c
    else:
        meio = c
        menor = a
if(c>=a and c>=b):
    maior = c
    if(a>=b):
        meio = a
        menor = b
        
    else:
        menor = a
        meio = b
        
a = maior
b = meio
c = menor
if (maior >= (meio+menor)):
    print("NAO FORMA TRIANGULO")
else:
    if (maior**2) == (meio**2 + menor**2):
        print("TRIANGULO RETANGULO")
        
    if (maior**2) > (meio**2+menor**2):
        print("TRIANGULO OBTUSANGULO")
        
    if ((maior**2) < ((meio**2)+(menor**2))):
        print("TRIANGULO ACUTANGULO")
        
    if (maior==meio and maior==menor):
        print("TRIANGULO EQUILATERO")
        
    if (maior==meio and maior!=menor) or (maior==menor and maior!=meio) or (menor==meio and menor!=maior):
        print("TRIANGULO ISOSCELES")