''' 
Given two string x and y
x: abcdgh
y: abedfhr
find longest common subsequence, here it is len(abdh) i.e. 4
'''

def lcs_recursive(x,y,n,m):
    # to write base condition, think of the smallest valid input
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        return 1 + lcs_recursive(x,y,n-1,m-1)
    else:
        return max(
            lcs_recursive(x, y, n-1, m),
            lcs_recursive(x, y, n, m-1)
        )

def lcs_memoize():
    pass

def lcs_tabulate():
    pass

if __name__ == "__main__":
    x =  "abcdgh"
    y =  "abedfhr"
    print("Recursive", lcs_recursive(x,y,len(x),len(y)))