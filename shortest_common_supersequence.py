'''                                    VARIANT OF LCS                                 '''

'''s
Given 2 strings:
a: "geek"
b: "eke"
Merge these 2 strings in shortest way possible, such that both the strings are present as 
subsequences in merged string aka supersequence. One answer is always tha concatenated string
but that may not be the shortest
In this example one way would be: geeke

Ex:
a:AGGTAB
b:GXTXAYB
Ans: AGGXTXAYB

Soln: length of shortest common supersequence: len(a)+len(b)-len(lcs(a,b))
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

if __name__=="__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    print("Length of SCS:", str(len(a)+len(b)-lcs_tabulate(a,b,len(a),len(b))))