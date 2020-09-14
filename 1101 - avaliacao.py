#Vitória Rocha
#Foi necessario utilizar o WHILE TRUE pq não se tinha ideia de quants vezes o programa seria executado,
#depois disso segui as ordens dadas no enunciado do exercicio

while True: #para q seja executado n vezes, indefinadamente
    try:
        #lendo
        m,n = input().split()
        #definindo-as como variavel INT
        m = int(m)
        n = int(n)
        if(m < 1 or n < 1 ): #qdo m ou n for menor q 0
            break #parar execução
        #variavel temporaria p receber valor de n caso n for maior q m
        temp = 0
        #se m > n
        if(m > n):
            #realiza a troca das duas variaveis p deixar ordenado do menor pro maior
            temp = m
            m = n
            n = temp
            
        #variavel p realizar a som e apresentar p usuario   
        soma = 0
        #string p mostrar valores entre m e n
        resultado = '' 
        
        #repetir enquanto m for menor ou igual a n
        while(m <= n):
            #transformará m em string e irá mostrar na tela
            resultado = resultado + str(m) + ' '
            #variavel soma somando os valores entre m e n para apresentar p usuario no final da execução
            soma = soma + m
            #adiciona +1 a variavel M para mostrar em ordem crescente os valores ate N
            m = m+1
        #resultado mostra os valores de M até N e a soma total, 'Sum=%d' é somado na string resultado para apresentar na tela
        resultado = resultado + 'Sum=%d'
        print(resultado %soma) #mostrando
        
    except: #nenhum valor dado como entrada
        break #parar execução 