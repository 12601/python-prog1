valor = input()
valor = int(valor)

troco = valor

n100 = troco//100
troco = troco - (n100*100)

n50 = troco//50
troco = troco - (n50*50)

n20 = troco//20
troco = troco - (n20*20)

n10 = troco//10
troco = troco -(n10*10)

n5 = troco//5
troco = troco - (n5*5)

n2 = troco//2
troco = troco - (n2*2)

print("\n",valor)
print(n100,"nota(s) de R$ 100,00\n")
print(n50,"nota(s) de R$ 50,00\n")
print(n20,"nota(s) de R$ 20,00\n")
print(n10,"nota(s) de R$ 10,00\n")
print(n5,"nota(s) de R$ 5,00\n")
print(n2,"nota(s) de R$ 2,00\n")
print(troco,"nota(s) de R$ 1,00\n")