"""
Leetcode #22 Generate all Valid Parenthesis

Solution using backtracking:
"""
def generateParenthesis(n):
    res=[]
    def backtrack(S,num_avail,num_unclosed):
        if num_avail==0:
            res.append(S+")"*num_unclosed)
            return
        if num_unclosed==0:
            backtrack(S+"(",num_avail-1,num_unclosed+1)
            return
        backtrack(S+"(",num_avail-1,num_unclosed+1)
        backtrack(S+")",num_avail,num_unclosed-1)
    backtrack("",n,0)
    return res
