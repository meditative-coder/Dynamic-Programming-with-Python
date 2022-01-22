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
    t = [[-1 for j in range(0,W+1)] for i in range(n+1)]
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
    t = [[-1 for j in range(0,W+1)] for i in range(n+1)]
    # This table is filled in 2 steps   
    
    for i in range(0,n+1):
        for j in range(0, W+1):
            ## 1. Intialization, similar to defining base case in recursion
            if i==0 or j==0:
                t[i][j] = 0

            ## 2. Convert recursive calls to iterative    
            #''' t[i][j] defines max_profit given first (i-1) elements and weight=j '''
            #''' t[n][W] defines max_profit given n elements and W weight'''
            elif weights[i-1] <= j:
                t[i][j] = max(
                    profits[i-1]+t[i-1][j-weights[i-1]],
                    t[i-1][j]
                )
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]

if __name__ == "__main__":
    weights = [10, 20, 30]
    profits = [60, 100, 120]
    W = 50
    n = 3
    print("Recursive: ", knapsack_recursive(weights, profits, W, n))
    print("Memoization: ", knapsack_memoize(weights, profits, W, n))
    print("Tabulation: ", knapsack_tabulate(weights, profits, W, n))