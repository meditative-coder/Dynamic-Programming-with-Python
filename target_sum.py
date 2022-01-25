'''                                       VARIANT OF 0-1 KNAPSACK                                    '''

'''
    Given an array: arr
    Given an value: sum
    We have to assign an operator, either + or - before every element\
    such that sum of resulting array = sum provided.
    Return: int, i.e. Count of such subsets
'''

'''
Approach: consider putting positive elements on one side and negative elements other side
then we just have to find sum(positive side) - sum(negative side) = given sum
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
    return t[n][sum]

if __name__ == "__main__":
    arr = [1,1,2,3]
    target_sum = 1
    n = 4
    sum_required = (target_sum+sum(arr))/2
    print("Count Found: ", knapsack_tabulate(arr, int(sum_required), n))