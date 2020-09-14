#Vitória Rocha
#Como não podia usar vetor criei uma variael pra cada entrada do usuario e fui comparando e fazendo a contagem de quantos numeros iguais tinha
#lendo os valores q foram escolhidos pelo usuario
x1,x2,x3,x4,x5,x6 = input().split()
#lendo os resultados sorteados na loteria
y1,y2,y3,y4,y5,y6 = input().split()
#transformando todas em INT
x1 = int (x1)
y1 = int (y1)
x2 = int (x2)
y2 = int (y2)
x3 = int (x3)
y3 = int (y3)
x4 = int (x4)
y4 = int (y4)
x5 = int (x5)
y5 = int (y5)
x6 = int (x6)
y6 = int (y6)
#variavel cont=0 para realizar a contagem de acertos
cont = 0
#verificando se x1 é igual a algum valor sorteado
if((x1 == y1) or (x1 == y2) or (x1 == y3) or (x1 == y4) or (x1 == y5) or (x1 == y6)):
    cont = cont+1 #se for, soma + 1
    
#verificando se x2 é igual a algum valor sorteado
if((x2 == y1) or (x2 == y2) or (x2 == y3) or (x2 == y4) or (x2 == y5) or (x2 == y6)):
    cont = cont+1 #se for, soma + 1
 
#verificando se x3 é igual a algum valor sorteado
if((x3 == y1) or (x3 == y2) or (x3 == y3) or (x3 == y4) or (x3 == y5) or (x3 == y6)):
    cont = cont+1 #se for, soma + 1

#verificando se x4 é igual a algum valor sorteado
if((x4 == y1) or (x4 == y2) or (x4 == y3) or (x4 == y4) or (x4 == y5) or (x4 == y6)):
    cont = cont+1 #se for, soma + 1
    
#verificando se x5 é igual a algum valor sorteado
if((x5 == y1) or (x5 == y2) or (x5 == y3) or (x5 == y4) or (x5 == y5) or (x5 == y6)):
    cont = cont+1 #se for, soma + 1

#verificando se x5 é igual a algum valor sorteado
if((x6 == y1) or (x6 == y2) or (x6 == y3) or (x6 == y4) or (x6 == y5) or (x6 == y6)):
    cont = cont+1 #se for, soma + 1
    
    
#mostrara pro usuario a qt de acertos

#menos q 3, mostra "azar"
if(cont < 3):
    print("azar")
    
#3 acertos, mostra "terno"
if(cont == 3):
    print("terno")
    
#4 acertos, mostra "quadra"
if(cont == 4):
    print("quadra")
    
#5 acertos, mostra "quina"
if(cont == 5):
    print("quina")

#5 acertos, mostra "sena"
if(cont == 6):
    print("sena")