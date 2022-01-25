'''                           VARIANT OF UNBOUNDED KNAPSACK                       '''

'''
Given an array of coins [1,2,3] and
given sum = 5,
find number of ways we can achieve the given sum given unlimited coins

It is very similar to count of subset with given sum.
Just change the condition from 0-1 to unbounded
'''

def knapsack_tabulate(arr, sum, n):
    t = [[0 for j in range(0,sum+1)] for i in range(n+1)]
    

    #                             Base Condition
    # if no item is given, we can't achieve the sum
    for j in range(0, sum+1):
        t[0][j] = 0

    # if sum=0, empty set is always the answer, thus True
    for i in range(n+1):
        t[i][0] = 1

    #                            Fill rest of the matrix
    for i in range(1,n+1):
        for j in range(1, sum+1):   
            # ''' t[i][j] defines Whether subset possible given first (i-1) elements and sum=j '''
            # This condition says that, only consider a element if it's value is less or equal to target
            if arr[i-1] <= j:
                t[i][j] = t[i][j-arr[i-1]] + t[i-1][j] # take or not
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]

if __name__ == "__main__":
    coins = [1,2,3]
    sum = 5
    print("Total number of changes", knapsack_tabulate(coins,sum,len(coins)))