#[0,25], (25,50], (50,75], (75,100])
#[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
#(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000
x = float(input())
if(x>=0 and x<=25):
    print('Intervalo [0,25]')
elif(x>25 and x<=50):
    print('Intervalo (25,50]')
elif(x>50 and x<=75):
    print('Intervalo (50,75]')
elif(x>75 and x<=100):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
    