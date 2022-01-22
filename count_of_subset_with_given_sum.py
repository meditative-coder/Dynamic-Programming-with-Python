'''                                       VARIANT OF 0-1 KNAPSACK                                    '''

'''
    Given an array: arr
    Given an value: sum
    Find the count of subsets present in array whose sum is equal to given sum value
    Return True/False
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
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j] # take or not
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][sum]

if __name__ == "__main__":
    arr = [2,3,5,6,8,10]
    sum=  10
    n = 6
    print("Sum Found: ", knapsack_tabulate(arr, sum, n))