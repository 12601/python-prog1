#ordenar_4_inteiros.ty
#Aluna: Vitória ROCHA
#lendo
t,u,v,x = input().split()
t = int(t)
u = int(u)
v = int(v)
x = int(x)

#posicionando o t
menor = t

if (menor > u):
    aux = u
    u = menor
    menor = aux

if (menor > v):
    aux = v
    v = menor
    menor = aux

if (menor > x):
    aux = x
    x = menor
    menor = aux

t = menor

#posicionando o u
menor = u

if (menor > v):
    aux = v
    v = menor
    menor = aux

if (menor > x):
    aux = x
    x = menor
    menor = aux
    
u = menor

#posicionando o v
menor = v

if (menor > x):
    aux = x
    x = menor
    menor = aux
    
v = menor

#x posicionado
print (t, u, v, x)