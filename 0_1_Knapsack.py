# Recursive
def knapsack_recursive(weights, profits, W, n):
    if n==0 or W==0:
        return 0
    if (weights[n-1]<=W):
        return max(
            profits[n-1]+knapsack_recursive(weights, profits, W-weights[n-1], n-1),
            knapsack_recursive(weights, profits, W, n-1)
        )
    elif (weights[n-1]>W):
        return knapsack_recursive(weights, profits, W, n-1)

# Memoization (top-down)
def knapsack_memoize(weights, profits, W, n):
    t = [[-1]*(W+1)]*(n+1)
    if n==0 or W==0:
        return 0
    if t[n][W] != -1:
        return t[n[W]]

    if (weights[n-1]<=W):
        t[n][W] =  max(
            profits[n-1]+knapsack_recursive(weights, profits, W-weights[n-1], n-1),
            knapsack_recursive(weights, profits, W, n-1)
        )
        return t[n][W]
    elif (weights[n-1]>W):
        t[n][W] = knapsack_recursive(weights, profits, W, n-1)
        return t[n][W]

# Tabulation(bottom up)
# Completely omit out the recursive calls, thus does not ends to stack overflow
def knapsack_tabulate(weights, profits, W, n):
    t = [[-1]*(W+1)]*(n+1)
    # This table is filled in 2 steps
    
    ## 1. Intialization, similar to defining base case in recursion


    ## 2. Convert recursive calls to iterative
    
    ''' t[i][j] defines max_profit given first (i-1) elements and weight=j '''
    ''' t[n][W] defines max_profit given n elements and W weight'''

