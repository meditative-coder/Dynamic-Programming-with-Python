''' 
Given two string x and y
x: abcdgh
y: abedfhr
find longest common subsequence, here it is len(abdh) i.e. 4
'''

def lcs_recursive(x,y,m,n):
    # to write base condition, think of the smallest valid input
    if n==0 or m==0:
        return 0
    if x[m-1]==y[n-1]:
        return 1 + lcs_recursive(x,y,m-1,n-1)
    else:
        return max(
            lcs_recursive(x, y, m-1, n),
            lcs_recursive(x, y, m, n-1)
        )

t = [[-1 for j in range(101)] for i in range(101)]
def lcs_memoize(x,y,m,n):
    global t
    if m==0 or n==0:
        return 0
    if t[m][n] != -1:
        return t[m][n]
    if x[m-1] == y[n-1]:
        t[m][n] = 1 + lcs_memoize(x,y,m-1,n-1)
        return t[m][n]
    else:
        t[m][n]= max(
            lcs_memoize(x,y,m-1,n),
            lcs_memoize(x,y,m,n-1)
        )
        return t[m][n]

def lcs_tabulate(x,y,m,n):
    t = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(
                    t[i-1][j],
                    t[i][j-1]
                )
    return t[m][n]

    

if __name__ == "__main__":
    x =  "abcdgh"
    y =  "abedfhr"
    print("Recursive", lcs_recursive(x,y,len(x),len(y)))
    print("Memoize", lcs_memoize(x,y,len(x),len(y)))
    print("Tabulation", lcs_tabulate(x,y,len(x),len(y)))