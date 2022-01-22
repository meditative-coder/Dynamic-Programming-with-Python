'''                                       VARIANT OF 0-1 KNAPSACK                                    '''

'''
    Given an array: arr
    Given an value: sum
    Divide arr in 2 partitions, such that that sum of elements of the two partions is equal
    Return True/False

    Ex: for input [1,5,11,5], two partitions are [1,5,5] and [11]. So return True
'''


''' Using same function from 0_1_Knapsack with minor modifications '''
def knapsack_tabulate(arr, sum, n):
    t = [[False for j in range(0,sum+1)] for i in range(n+1)]
    

    #                             Base Condition
    # if no item is given, we can't achieve the sum
    for j in range(0, sum+1):
        t[0][j] = False

    # if weight=0, empty set is always the answer, thus True
    for i in range(n+1):
        t[i][0] = True

    #                            Fill rest of the matrix
    for i in range(1,n+1):
        for j in range(1, sum+1):   
            # ''' t[i][j] defines Whether subset possible given first (i-1) elements and sum=j '''
            # This condition says that, only consider a element if it's value is less or equal to target
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j] # take or not
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]

if __name__ == "__main__":
    arr = [1,6,11,5]
    n = 4
    # Commmon sense: To divide an array into 2 equal sum partitions, the sum of array must be even
    if sum(arr)%2==0:
        # Now we just need to find a subset whose sum is sum(arr)/2.
        # Now the problem is similar to subset sum problems
        print("Partition Found?",knapsack_tabulate(arr,sum(arr)//2,n))
    else:
        print("Partition canno be done for elements whose element sum is odd")