# coding: utf-8
import Matrizes
"""
    MILENA ALEGRE E VITÓRIA ROCHA
"""
print("Dimensão das matrizes de teste: ", end="")
dim = input().split()
m = int(dim[0])
n = int(dim[1])
print("Cria e lê uma matriz S {0:d}x{1:d} de strings:".format(m, n))
S = Matrizes.cria(m, n)
Matrizes.le(S, m, n)

print("Cria uma matriz A e coloca a matriz S transformada em int nela:")
A = Matrizes.cria(m, n)
Matrizes.str2int(S, A, m, n)
Matrizes.mostra(A, m, n)

print("Cria e lê uma matriz T {0:d}x{1:d} de strings:".format(m, n))
T = Matrizes.cria(m, n)
Matrizes.le(T, m, n)

print("Cria uma matriz B e coloca a matriz T transformada em int nela:")
B = Matrizes.cria(m, n)
Matrizes.str2int(T, B, m, n)
Matrizes.mostra(B, m, n)

print("Cria uma matriz Soma e coloca nela a soma das matrizes A e B:")
Soma = Matrizes.cria(m, n)
Matrizes.soma(A, B, Soma, m, n)

print("Mostra a matriz Soma:")
Matrizes.mostra(Soma, m, n)

print("Cria uma matriz Sub e coloca nela A-B:")
Sub = Matrizes.cria(m, n)
Matrizes.subtrai(A, B, Sub, m, n)

print("Mostra a matriz Sub:")
Matrizes.mostra(Sub, m, n)

print("Mostra a coluna 0 da matriz A:")
coluna = Matrizes.col(A, 0, m, n)
for i in range(m):
    print(coluna[i])
    
print("Mostra a linha 0 da matriz A:")
linha = Matrizes.lin(A, 0, m, n)
for i in range(n):
    print(linha[i], "", end="")
print()
    
print("Mostra a diagonal principal da matriz A:")
diagp = Matrizes.diagpr(A, m, n)
for i in range(len(diagp)):
    print(diagp[i], "", end="")
print()
    
print("Mostra a diagonal secundária da matriz A:")
diags = Matrizes.diagsec(A, m, n)
for i in range(len(diags)):
    print(diags[i], "", end="")
print()

print("\nMultiplicação matrizXmatriz\n")
print("\nEntre com o nº de linhas matriz A: ")
la = int (la)
            
print("\nEntre com o nº de colunas matriz A: ")
ca = int (ca)
            
print("\nEntre com o nº de linhas matriz B: ")
lb = int (lb)

while(True):
    if(lb != ca):
        lb = int (lb)

print("\nEntre com o nº de colunas matriz B:\n")
cb = int (cb)

print("\nInsira os valores matriz A:\n")
Matrizes.le(ma, la, ca)
                    
print("\nInsira os valores matriz B:\n")
Matrizes.le(mb, lb, cb)
            
print("\nMatriz A:\n")
Matrizes.mostra(ma, la, ca)
                    
print("\nMatriz B:\n")
Matrizes.mostra(mb, lb, cb)
            
print("\nMatriz C:\n")
Matrizes.multiplica(ma, mb, mc, la, cb, ca)
