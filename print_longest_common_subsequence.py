'''                                VARIANT OF LCS                                     '''
'''
Given 2 strings, print the longest common subsequence between them
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
    # Logic for printing LCS
    i = m
    j = n
    res = ""
    while i > 0 and j>0:
        if x[i-1]==y[j-1]:
            res = res+x[i-1]
            i = i-1
            j = j-1
        else:
            if t[i-1][j]>t[i][j-1]:
                i = i-1
            else:
                j = j-1
    res = res[::-1]
    return res

    

if __name__ == "__main__":
    x =  "ankit"
    y =  "harshita"
    print("Tabulation:", lcs_tabulate(x,y,len(x),len(y)))
