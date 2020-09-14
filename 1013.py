a,b,c = input().split()
a = int (a)
b = int (b)
c = int (c)

if (a>b & a>c):
    print(a, "eh o maior")
elif (b>a & b>c):
    print(b, "eh o maior")
else:
    print(c, "eh o maior")