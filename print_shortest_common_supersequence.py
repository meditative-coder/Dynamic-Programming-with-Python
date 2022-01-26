'''                                    VARIANT OF LCS                                 '''

'''s
Given 2 strings:
a: "geek"
b: "eke"
Merge these 2 strings in shortest way possible, such that both the strings are present as 
subsequences in merged string aka supersequence. One answer is always the concatenated string
but that may not be the shortest
In this example one way would be: geeke

Ex:
a:acbcf
b:abcdaf
Ans: acbcdaf

Print the result
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
    print(t[m][n])
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
                res = res + x[i-1]
                i = i-1
            else:
                res = res + y[j-1]
                j = j-1
    while i>0:
        res = res + x[i-1]
        i = i-1
    while j>0:
        res = res + y[j-1]
        j = j-1
    res = res[::-1]
    return res

    

if __name__ == "__main__":
    x =  "abac"
    y =  "cab"
    print("Tabulation:", lcs_tabulate(x,y,len(x),len(y)))
