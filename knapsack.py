# ex 3
it = 0
def knapSack(W, wt, val, n):
    # Base Case
    global it
    it += 1
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
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
  
# end of function knapSack

def knapSackPD(N, C, itens): #INCOMPLETO, NÃO FUNCIONA
   #N = número de produtos;
   #C = capacidade real da mochila
   # itens[0](0,0);   # (O índice 0 guarda null), Tupla com peso e valor
   maxTab = [ [ 0 for i in range(N + 1) ] for j in range(C + 1) ]

   #Inicialize com 0 toda a linha 0 e também a coluna 0;
   for i in range(1,N):
      for j in range(1,C):
         if(itens[i][1] <= j): # se o item cabe na mochila atual
            maxTab[j][i] = max(maxTab[j-1][i], 
                               itens[i][0] + 
                                 maxTab[j-1][i - itens[i][1]]);
         else:
            maxTab[j][i] = maxTab[j-1][i]

   return maxTab[C][N]  # valor máximo para uma mochila de capacidade C e 		         
                        # que pode conter itens que vão do item 1 até o item N.

print(knapSackPD(5,15,[(4,12),(2,1),(10,4),(1,1),(2,2)]))