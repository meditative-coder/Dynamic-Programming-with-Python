'''                           VARIANT OF UNBOUNDED KNAPSACK                       '''

'''
Given a rod of length l, we need to cut it into peices.
We are given a price of every length of cut.
Cut the rod into pieces in a way that the price(profit) is maximum

N = 8 (length of rod)
length: [1,2,3,4,5,6,7,8]
price:  [1,5,8,9,10,17,17,20]

Similarity with knapsack: N is similar to W, wt is similar to length, val is similar to price
Since, we can have 2 cuts of similar length, so it is variant of unbounded knapsack

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
    N = 8

    ## Sometimes it may be case that 1-N are not given in length. 
    ## i.e. We have constraints on length we can cut rod in
    length = [1,2,3,4,5,6,7,8]
    price =  [1,5,8,9,10,17,17,20]
    print("Max Price: ", unbounded_knapsack_tabulate(length, price, N, len(length)))
