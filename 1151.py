x = input()
x = int(x)
a = 1
b = 1
c = 0
cont = x
while(x>0 and x<46):
    if (cont == x):
        print("0", end=" ")
        x = x-1
    else:
        if(x < 2):
            a = b+c
            b = c
            c = a
            print(c)
            x = x-1
        else:
            a = b+c
            b = c
            c = a
            print(c, end= " ")
            x = x-1
