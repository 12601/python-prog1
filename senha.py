#Vitória Rocha
#Primeiro leio a senha e crio uma variavel int de valor 0.
senha = input()
#enquanto x =! da senha ele realiza a repetição
x = 0
while x != senha:
    x = input()
    if(x!=senha):
        #se entrar nesse if significa que a senha digitada esta errada, ent mostra a mensagem:
        print("Senha incorreta!")
#quando sair do while significa que acertou a senha, ent mostra a mensagem:
print("Você adivinhou a senha!")