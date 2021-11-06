import numpy as np
import itertools

def random_matrix(dim):
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def znak(perestanovka):
    z = 1
    for i in range(len(perestanovka)):
        for j in range(i,len(perestanovka)):
            if perestanovka[i] > perestanovka[j]:
                z = -1*z
    return z

def summa(dim, matriza):
    sum = 0
    for i in perestanovki(dim):
        sum += znak(i)*proizvedenie(i, dim, matriza)
    return sum

def perestanovki(dim):
    s = '123456789'     
    return list(itertools.permutations(s[:dim], dim))

def proizvedenie(perestanovka, dim, matriza):
    pr = 1
    for i in range(dim):
        pr *= matriza[i][int(perestanovka[i])-1]
    return pr

#Input block
n = int(input())
if n>0:
    m = random_matrix(n)
    print(m)
    print(summa(n,m)