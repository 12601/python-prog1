n = int(input())
fatorial = n
if(n>0 and n<13):
    for i in range(n-1, 1, -1):
        fatorial = fatorial * i
print(fatorial)    