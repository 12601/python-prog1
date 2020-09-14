x = int(input())

while (x != 0):
    somam = 0
    somaj = 0
    for i in range(0,6):
        if(i<3):
            joaop, joaod = input().split()
            joaop, joaod = int(joaop), int(joaod)

            somaj = somaj + (joaop * joaod)
            
        if(i>=3 and i<6):
            mariap, mariad = input().split()
            mariap, mariad = int(mariap), int(mariad)
            
            somam = somam + (mariap * mariad)
    if(somaj > somam):
        print('JOAO')
    else:
        print('MARIA')
    
    x = x-1
    
