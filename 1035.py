a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
somaC = c+d
somaA = a+b
if ((a%2==0) and (c>=0 and d>=0) and (somaC>somaA) and (b>c and d>a)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")