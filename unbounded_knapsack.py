'''
In 0-1 Knapsack we either choose element or not

But in unbounded knapsack, we can include an element multiple times.
1. If not selected at any time, we will not come to it again. Processed state
2. If selected at any time, we may come to it again later. Unprocessed state
'''
def unbounded_knapsack_tabulate(weights, profits, W, n):
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
                    # difference with 0-1 knapsack is just that i-1 is not done, i.e item is still considered
                    profits[i-1]+t[i][j-weights[i-1]],
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
    print("Max Profit: ", unbounded_knapsack_tabulate(weights, profits, W, n))