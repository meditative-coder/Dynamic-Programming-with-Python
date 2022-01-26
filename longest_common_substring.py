'''                                     VARIANT OF LCS                                       '''

def lcs_tabulate(x,y,m,n):
    t = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            # this else condition is only different with longest common subsequence
            ## Instead of selecting max, on discontinuity start from 0
            else:
                t[i][j] = 0
    current_max = 0
    for i in range(m+1):
        for j in range(n+1):
            if t[i][j] > current_max:
                current_max = t[i][j]
    return current_max

    

if __name__ == "__main__":
    x =  "abcdef"
    y =  "abchfg"
    print("Tabulation", lcs_tabulate(x,y,len(x),len(y)))