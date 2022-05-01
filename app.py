from dis import dis
from glob import glob
from tkinter import N
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time

# ex 1
ite = 0

def fiboRec(n):
    global ite
    ite += 1
    if n <= 1:
        return n
    return fiboRec(n-1) + fiboRec(n-2)

def fibo(n):
    global ite
    f = [0]
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        ite += 1
    return ite

#print(fiboRec(30))

def memoFib(n):
    f = [-1] * (n+1)
    #print(f)
    return lookUpFib(f,n)

def lookUpFib(f,n):
    global ite
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        ite +=1
        f[n] = lookUpFib(f, n-1) + lookUpFib(f, n-2)
    return f[n]

print(memoFib(180) , ite)

# Resultados
'''
Entrada     Ite Rec     Normal      Memo
10          177         9           9
20          21891       19          19
30          2692537     29          29
40                      39          39
                        Linear      Linear  
'''

# Criacao de grafico
'''
x = []
y = []
for n in range(10000):
    x.append(n)
    y.append(fibo(n))

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x, y);  # Plot some data on the axes.
ax.set_title("fibo10000")
ax.set_xlabel('Entrada')
ax.set_ylabel('Iteracoes')
fig.savefig('fibo10000.png')
'''  
