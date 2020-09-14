x, y = input().split()
x = int(x)
y = int(y)
if(x == 1):
    total = y*4
elif (x == 2):
    total = y*4.5
elif (x == 3):
    total = y*5
elif (x == 4):
    total = y*2
elif (x == 5):
    total = y*1.5

total = float(total)
print("Total: R$ {0:4.2f}".format(total))
