a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if ((a < b) and (b < c)):
    print(a)
    print(b)
    print(c)
        
elif ((a < c) and (c < b)):
    print(a)
    print(c)
    print(b)
        
elif ((b < a) and (a < c)):
    print(b)
    print(a)
    print(c)
        
elif((b < c) and (c < a)):
    print(b)
    print(c)
    print(a)
        
elif((c < a) and (a < b)):
    print(c)
    print(a)
    print(b)
        
else:
    print(c)
    print(b)
    print(a)
    
print("\n")

print(a)
print(b)
print(c)