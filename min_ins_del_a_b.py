'''                                  VARIANT OF LCS                                     '''
'''
Given 2 strings:
a = "heap"
b = "pea"
We need to find the minimum number of insertion and deletion to make in string "a" to
convert it to string b

Solution:
delete h, insert p, delete last p, thus 3 operations
logic: common subsequence is untouched
# no of deletion: len(a)-lcs
# no of insertion: len(b)-lcs
therefore total ops = len(a)+len(b)-2*lcs
'''

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
    x =  "ankit"
    y =  "chouhan"
    min_ops = len(x)+len(y)-2*lcs_tabulate(x,y,len(x),len(y))
    print("Min Operations", min_ops)