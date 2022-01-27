'''                                   VARIANT OF LCS                                   '''

'''
Given string:
a = "aebebda"
Find the minimum number of deletions to be done in string "a" to make it palindrome
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
    x =  "agbcba"
    print("Min Deletions", len(x)-lcs_tabulate(x,x[::-1],len(x),len(x)))
