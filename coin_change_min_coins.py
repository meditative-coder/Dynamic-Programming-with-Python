'''                           VARIANT OF UNBOUNDED KNAPSACK                       '''

'''
Given an array of coins [1,2,3] and
given sum = 5,
find minimum number of coins we can achieve the given sum given unlimited coins

It is very similar to count of subset with given sum.
Just change the condition from 0-1 to unbounded
'''

def knapsack_tabulate(arr, sum, n):
    t = [[0 for j in range(0,sum+1)] for i in range(n+1)]
    

    #                             Base Condition

    for i in range(n+1):
        t[i][0] = 0
    for j in range(0, sum+1):
        t[0][j] = float('inf')
    for j in range(1, sum+1):
        if j%arr[0] !=0:
            t[1][j] = float('inf')
        else:
            t[1][j] = 1

    # This question is unique in it's own, because we also need to initialize 2nd row in it

    

    #                            Fill rest of the matrix
    for i in range(1,n+1):
        for j in range(1, sum+1):   
            # ''' t[i][j] defines Whether subset possible given first (i-1) elements and sum=j '''
            # This condition says that, only consider a element if it's value is less or equal to target
            if arr[i-1] <= j:
                t[i][j] = min(1+ t[i][j-arr[i-1]] , t[i-1][j]) # take or not
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]



if __name__ == "__main__":
    coins = [1,2,3]
    sum = 5
    print("Minimum coins for change", knapsack_tabulate(coins,sum,len(coins)))