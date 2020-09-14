#lendo
k = int(input())
l = int(input())
if k < 1 or k > 16 or k == l or l < 1 or l > 16: #verificando se a entrada é valida
  print ("entrada inválida!")
elif k < 9 and l >= 9 or l < 9 and k >= 9:
  print ("final")

if k > l:
    if k >= 5 and l < 5 or k >= 13 and l >= 9 and l < 13:
        print ("sandmifinal")
    if k%2 == 0 and l == k - 1:
        print ("oitavas")
    if k - l == 1 or k - l == 2 or k - l == 3:
        print ("quartas")
        
if l > k:
    if l >= 5 and k < 5 or l >= 13 and k >= 9 and k < 13:
        print ("semifinal")
          
    if l%2 == 0 and k == l:
        print ("oitavas")

    if l - k == 1 or l - k == 2 or l - k == 3:
        print ("quartas")
