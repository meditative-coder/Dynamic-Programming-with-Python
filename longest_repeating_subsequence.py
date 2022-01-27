'''                                     VARIANT OF LCS                                 '''
'''
Given a string "a", find the length of longest repeating subsequence in it
'''

def lcs_tabulate(x,y,m,n):
    t = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif x[i-1] == y[j-1] and i != j:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(
                    t[i-1][j],
                    t[i][j-1]
                )
    return t[m][n]

    

if __name__ == "__main__":
    x =  "aabebcdd"
    print("Tabulation", lcs_tabulate(x,x,len(x),len(x)))