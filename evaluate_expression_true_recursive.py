'''                                      VARIANT OF MCM                             '''

'''
Given string of T(True) and F(False), and operators(and '&',or '|' and xor '^') between them.
We need to find the number of ways of parenthesization order such that input string is evaluated to True.
Ex: s = "T^F&T"
    O/P: 2 , ((T^F)&T) and T^(F&T)
'''
def mcm_recursive(s):
    def solve(s, i, j, istrue):
        # Base condition
        # If string is empty or single character or string itself is palindrome,
        # no partition needed
        if i>j:
            return False
        if i==j:
            if istrue==True:
                return s[i]=='T'
            else:
                return s[i]=='F'


        ans = 0
        for k in range(i+1,j,2):

            lt = solve(s,i,k-1,True)
            lf = solve(s,i,k-1,False)
            rt = solve(s,k+1,j,True)
            rf = solve(s,k+1,j,False)

            if s[k]=='&':
                if istrue==True:
                    ans = ans + lt*rt
                else:
                    ans = ans + lt*rf + lf*rt + lf*rf

            elif s[k]=='|':
                if istrue == True:
                    ans = ans + lt*rt + lt*rf + lf*rt
                else:
                    ans = ans + lf*rf
                
            elif s[k]=='^':
                if istrue == True:
                    ans = ans + lt*rf + lf*rt
                else:
                    ans = ans + lt*rt + lf*rf

        return ans
    return solve(s,0,len(s)-1, True)

if __name__ == "__main__":
    s = "T^F&T"
    print("MCM Recursive", mcm_recursive(s))