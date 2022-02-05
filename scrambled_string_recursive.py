'''                                         VARIANT OF MCM                                '''
##########################################  5-star problem  ################################

'''
Given 2 strings:
a = "great"
b = "rgeat"
Find if a and b are scrambled strings.
Scrambled strings:
1st constraint: you can only make binary tree from string
Ex: great -> gr, eat -> ((g,r), (e,at) or (ea,t)) -> ((gr), (e, (a,t)), ((e,a),t))
2nd constraint: No child can be empty

We can do swapping at non-leaf nodes, 0 or more times 

O/P: True/False
'''

from enum import Flag


def solve(a:str,b:str) -> bool:
    if len(a)!=len(b):
        return False
    if a==b:
        return True
    if len(a)<=1:
        return False
    n = len(a)
    flag = False
    for i in range(1, n):
        #                  Condition for swap                          Condition for no swap
        if (solve(a[-i:],b[:i]) and solve(a[:-i],b[i:])) or (solve(a[0:i], b[0:i]) and solve(a[i:],b[i:])):
            flag = True
            break
    return flag
if __name__ == "__main__":
    print("Is Scrambled ", solve('abcde','caebd'))