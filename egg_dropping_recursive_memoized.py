'''                              VARIANT OF MCM                             '''
###################        Fundamental problem of DP     ####################
'''
Given number of eggs(e) and number of floors of building(f).
We need to find the minimum numbers of attempts in worst case,
Find the threshold floor:
If egg dropped from above than threshold floor, it will break.
If egg dropped from below than threshold floor, it will not break.
Return the minimum number of attempts in finding the threshold floor.
'''

t = [[-1 for j in range(10001)] for i in range(10001)]
def solve(e, f) -> int:
    if f==0 or f==1:
        return f

    # if only one egg is given, drop egg from each floor, starting from below
    if e==1:
        return f

    if t[e][f]!=-1:
        return t[e][f]
    
    min_ = float('inf')
    
    for k in range(1,f+1):
        # We are doing max to consider the worst case
        temp = 1 + max(solve(e-1,k-1), solve(e,f-k))
        min_ = min(min_,temp)

    t[e][f] = min_
    return min_

if __name__=="__main__":
    print("Minimum attempts",solve(76,5465))