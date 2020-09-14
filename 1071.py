X = int(input())
Y = int(input())
soma = 0

if X == Y:
    print('0')
elif X < Y:
    for X in range(X,Y):
        X = X+1
        if X%2 != 0:
            soma= soma+X
else:
    for Y in range(Y,X):
        Y=Y+1
        if (Y%2==1) or (Y%2 == -1):
            soma= soma+Y
print(soma)