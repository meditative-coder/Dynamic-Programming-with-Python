'''                                 VARIANT OF MCM                                     '''
'''
Given a string s:
s = "nitin:
Find the minimum number of partitions we need to do,
Such that each substring after partition is palindrome.
Max answer is always len(s)-1, because a single character is always palindrome
'''

def mcm_recursive(arr):
    def solve(arr, i, j):
        # Base condition
        # If string is empty or single character or string itself is palindrome,
        # no partition needed
        if i>=j or arr[i:j]==arr[j:i:-1]:
            return 0
        min_ = float('inf')
        for k in range(i,j):
            temp = solve(arr, i, k) + solve(arr,k+1,j) + 1
            if temp  < min_:
                min_ = temp
        return min_
    return solve(arr,0,len(arr)-1)

if __name__ == "__main__":
    s = "badbab"
    print("MCM Recursive", mcm_recursive(s))