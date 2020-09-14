# coding:utf-8
"""
    MILENA ALEGRE E VITÓRIA ROCHA
"""

def cria(m, n):
    """
    Cria e retorna uma matriz de dimensão m x n.
    """
    mat = []
    for i in range(m):
        lin = [None]*n
        mat += [lin]
    return mat

def le(A, m, n):
    """
    Lê da entrada cada linha da matriz A. Assume que
    os valores da linha estão separados por espaço.
    """
    for i in range(m):
        lin = input().split()
        for j in range(n):
            A[i][j] = lin[j]

def str2int(Mstr, Mint, m, n):
    """
    Transforma a matriz Mstr de strings na
    matriz Mint de inteiros.
    """
    for i in range(m):
        for j in range(n):
            Mint[i][j] = int(Mstr[i][j])
            
def str2float(Mstr, Mfl, m, n):
    """
    Transforma a matriz Mstr de strings na
    matriz Mfl de números reais.
    """
    for i in range(m):
        for j in range(n):
            Mfl[i][j] = float(Mstr[i][j])
            
def soma(A, B, C, m, n):
    """
    Soma a matriz A com a B e coloca o resultado em C.
    """
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
            
def subtrai(A, B, C, m, n):
    """
    Subtrai a matriz B da matriz A e coloca o resultado em C.
    """
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
            
def col(A, c, m, n):
    """
    Retorna a coluna c da matriz A de dimensão m x n.
    """
    C = []
    for l in range(m):
        C += [A[l][c]]
    return C

def lin(A, l, m, n):
    """
    Retorna a linha l da matriz A de dimensão m x n.
    """
    L = []
    for c in range(n):
        L += [A[l][c]]
    return L

def diagpr(A, m, n):
    """
    Retorna a diagonal principal da matriz A de dimensão m x n.
    """
    D = []
    R = m
    if (m > n):
        R = n
    for i in range(R):
        D += [A[i][i]]
    return D

def diagsec(A, m, n):
    """
    Retorna a diagonal secundária da matriz A de dimensão m x n.
    """
    D = []
    R = m
    if (m > n):
        R = n
    j = n-1
    for i in range(R):
        D += [A[i][j]]
        j -= 1
    return D

def mostra(A, m, n):
    """
    Mostra a matriz A de dimensão m x n.
    """
    for i in range(m):
        for j in range(n):
            print(A[i][j], "", end="")
        print()

def multiplica(ma, mb, mc, m, n, ca):
    for i in range(m):
        print("\n")
        for j in range(n):
            if(ca == 1):
                mc[i][j] = ma[i][0] * mb[0][j]  
                print(mc[i][j] + "\t")
        
            elif(ca == 2):
                mc[i][j] = ma[i][0] * mb[0][j] + ma[i][1] * mb[1][j]                
                print(mc[i][j] + "\t")
                
            elif(ca == 3):
                mc[i][j] = ma[i][0] * mb[0][j] + ma[i][1] * mb[1][j] + ma[i][2] * mb[2][j]  
                print(mc[i][j] + "\t")
                
            elif(ca == 4):
                mc[i][j] = ma[i][0] * mb[0][j] + ma[i][1] * mb[1][j] + ma[i][2] * mb[2][j] + ma[i][3] * mb[3][j]
                print(mc[i][j] + "\t")
        
    
