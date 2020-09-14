#Vitória Rocha

#ESPECIFICAÇÕES DO EXERCICIO#
#Considerando o nosso alfabeto de 26 letras, uma frase é dita “completa” quando ela contém todas as letras do alfabeto contidas nela. De modo semelhante, uma frase é dita “quase completa” se ela não é completa, porém contém ao menos metade das letras do alfabeto contidas nela. Quando uma frase não é “completa” e nem “quase completa”, ela é dita “mal elaborada”.

#Primeiro leio x (quantidade de frases), depois um for é utilizado para ler a qt x de frases digitada pelo usuario. Um vetor (lista) é utilizado para dispor as letras do alfabeto e outro for é utilizado para ver se a letra está na frase digitada e caso estiver é adicionado +1 a variavel contadora. Por fim, de acordo com o valor da variavel contadora os IF's determinam se a frase é completa, incompleta ou mal elborada

#Lendo a qt de testes
x = int(input())
#For para rodar cada qt de teste
for i in range(x):
    #Lendo a frase e eliminando caracteres especiais e espaçamento deixnado em caixa alta
    frase = input().upper()
    #variavel contadora para fazer a contagem das letras
    cont=0
    #lista com as letras do alfabeto
    lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #for para fazer a verificação de letras na frase
    for letra in lista:
        #se a letra da vez estiver na frase é adicionado +1 na variavel contadora
        if (letra in frase):
            cont = cont+1

    #se cont for = 26, ou seja atende as especificações do exercicio
    if (cont >= 26):
         print('frase completa') #então é mostrador pro usuário "frase completa"

    #se cont for > 13, ou seja atende pelo menos metade das especificações do exercicio
    elif (cont > 13):
         print('frase quase completa')#então é mostrador pro usuário "frase incompleta"

    #se não tem nenhuma das especificações
    else:
         print('frase mal elaborada')#então é mostrador pro usuário "frase mal elaborada"