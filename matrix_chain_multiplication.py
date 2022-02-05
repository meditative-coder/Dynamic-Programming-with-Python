'''
Format to solve problems based on MCM

def solve(arr, i, j): -> int
    # Base Condtion (First Invalid Input)
    if (i>j):
        return 0
    # break at each k, where k lies between i and j
    for k in range(i,j):
        # Calculate temporary answer
        temporary = solve(arr,i,k) +(or any other operation) solve(arr,k+1,j)
        ans = func(temporary) 

'''

'''
Problem statement:
Given matrices:
A1, A2, A3,....An
We need to multiply these matrices in such a way that cost is minimum(no of multiplications is minimum)
arr = [40, 20, 30, 10, 30]
len(arr)=n-1
It means A1.shape = (40,20), A2.shape = (20,30)....
cost of multiplying A1 and A2 or no. of multiplications= 40 X 20 X 30

'''

def mcm_recursive(arr):
    def solve(arr, i, j):
        # Base condition
        if i>=j:
            return 0
        min_ = float('inf')
        for k in range(i,j):
            temp = solve(arr, i, k) + solve(arr,k+1,j) + (arr[i-1] * arr[k]* arr[j]) 
            # Cost of multiplying i to k + k+1 to j and cost of multiplying these resultant matrices
            if temp  < min_:
                min_ = temp
        return min_
    return solve(arr,1,len(arr)-1)

def mcm_memoize(arr):
    t = [[-1 for l in range(len(arr)+1)] for m in range(len(arr)+1)]
    def solve(arr, i, j):
        
        # Base condition
        if i>=j:
            return 0
        if t[i][j] != -1:
            return t[i][j]
        min_ = float('inf')
        for k in range(i,j):
            temp = solve(arr, i, k) + solve(arr,k+1,j) + (arr[i-1] * arr[k]* arr[j]) 
            # Cost of multiplying i to k + k+1 to j and cost of multiplying these resultant matrices
            if temp  < min_:
                min_ = temp
        t[i][j] = min_
        return min_
    return solve(arr,1,len(arr)-1)


if __name__ == "__main__":
    arr = [40,20,30,10,30]
    print("MCM Recursive", mcm_recursive(arr))
    print("MCM Memoized", mcm_memoize(arr))
    
