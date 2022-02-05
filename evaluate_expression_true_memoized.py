'''                                      VARIANT OF MCM                             '''

'''
Given string of T(True) and F(False), and operators(and '&',or '|' and xor '^') between them.
We need to find the number of ways of parenthesization order such that input string is evaluated to True.
Ex: s = "T^F&T"
    O/P: 2 , ((T^F)&T) and T^(F&T)
'''
def mcm_recursive(s):

    ### There are 2 ways we can proceed with memoization
    # 1. 
        # Here we need to create 3-D matrix, because with i and j, isTrue parameter is also changing,
        # which can take 2 values (True or False)
        # Disadvantage: Difficult to imagine
#    t = [[[-1 for l in range(2)] for m in range(101)] for n in range(101)]

    # 2. We can create a dictionary with keys in form (i<space>j<space>istrue) and corresponding answer as value
    t = dict()
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


        if str(i)+str(j)+str(istrue) in t.keys():
            return t[str(i)+str(j)+str(istrue)]

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
        t[str(i)+str(j)+str(istrue)] = ans
        return ans
    return solve(s,0,len(s)-1, True)

if __name__ == "__main__":
    s = "T^F&T"
    print("MCM Memoized", mcm_recursive(s))