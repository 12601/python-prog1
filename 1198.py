while True:
    try:
        x, y = input().split()
        x,y = int(x), int(y)
        diferenca = x-y
        
        if(diferenca<0):
            diferenca = diferenca * -1
            print(diferenca)
            
        elif(diferenca>=0):
            print(diferenca)
    except:
        break