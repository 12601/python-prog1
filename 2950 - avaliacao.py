#Vitória Rocha

#atribui esses valores para q consiga entrar no WHILE
d = 1 
x = 1
y = 1

#definindo as restrições das entradas do usuario
while((d>0 and d<100) and (x>0 and x<100) and (y>0 and y<100)):
    #lendo valores na mesma linha
    d, x, y = input().split() 
    #definindo como variavel int
    d = int(d)
    x = int(x)
    y = int(y)
    
    #formula p calcular ICM
    icm = d / (x+y)
    
#mostrando p usuario
print ("{0:4.2f}".format(icm))