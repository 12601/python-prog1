#abc.py
#Aluna: Vitória Rocha
#Para saber se está em ordem crescente foi necessario verificar se o primeiro numero digitado era o MENOR e se o ultimo era o MAIOR,
#porém pode haver a possibilidade de serem numeros repetidos, por isso utilizei >= e <=

#variaveis lidas na mesma linha
a,b,c = input().split()
#Linhas 9,10 e 11: convertendo a variavel p valor inteiro p fazer a comparação >, < OU =
a = int(a)
b = int(b) 
c = int(c)
#verificando se *a* é menor ou igual a *b* e se *b* é menor ou igual a *c*
if(a <= b <= c):
    #se for TRUE, aparece 'CRESCENTE' para o usuario, ou seja está na ordem crescente
    print('CRESCENTE')
#senao aparece 'NÃO CRESCENTE'
else:
    print('NÃO CRESCENTE')
    
#FIM :)