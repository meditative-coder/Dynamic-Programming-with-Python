'''                                       VARIANT OF 0-1 KNAPSACK                                    '''

'''
    Given an array: arr
    Given an value: sum
    Divide arr in 2 partitions, such that that difference of sum of elements of the two partions is minimum
    Return int

    Ex: for input [1,6,11,5], two partitions are [1,6,5] and [11], min difference = 1
'''

# Hint: This is mostly similar to equal sum partion.
# In Equal sum partition we need to do s1-s2= 0, here we need s1-s2=min


def minimumDifference(nums) -> int:
    def subset_sum_last_row(arr, _sum, n):
        t = [[False for j in range(0,_sum+1)] for i in range(n+1)]
        for j in range(0, _sum+1):
            t[0][j] = False
            
        for i in range(n+1):
            t[i][0] = True
            
        for i in range(1,n+1):
            for j in range(1, _sum+1): 
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j] # take or not
                else:
                    t[i][j] = t[i-1][j]
        
        # Instead of returning t[n][sum], return whole last row
        return t[-1]
    
    to_consider_array = subset_sum_last_row(nums,sum(nums),len(nums))
    mn = float('inf')
    higher_range = int(len(to_consider_array)/2)
    for i in range(0, higher_range):
        if to_consider_array[i]==True:
            mn = min(mn,sum(nums)-2*i)
    return mn

if __name__=="__main__":
    arr = [1,5,11,6]
    print("Minimum Difference is, ", minimumDifference(arr))