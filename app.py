import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time

ite = 0

def fiboRec(n):
    global ite
    ite += 1
    if n <= 1:
        return n
    return fiboRec(n-1) + fiboRec(n-2)

def fibo(n):
    ite = 0
    f = [0]
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        ite += 1
    return ite

def knapSack(W, wt, val, n):
  
    # Base Case
    if n == 0 or W == 0:
        return 0
  
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
  
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return list(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
  
# end of function knapSack
  
  
#Driver Code
val = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
wt = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
W = 165
n = len(val)
print(knapSack(W, wt, val, n))
  
# This code is contributed by Nikhil Kumar Singh

#x = []
#y = []
#for n in range(10000):
#    x.append(n)
#    y.append(fibo(n))
#
#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot(x, y);  # Plot some data on the axes.
#ax.set_title("fibo10000")
#fig.savefig('fibo10000.png')

