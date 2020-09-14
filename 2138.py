i = 0
cont = 0
maior = 0
while True:
    try:
        n = input()
        ls = len(n)
        maior = cont[0]
        for i in range (ls):
            if(n[i]==n[ls]):
                cont[i] = cont[i] + 1

        for i in range (ls):
            if(cont[i] > maior):
                maior = cont[i]
    except EOFError:
        break
print(maior)