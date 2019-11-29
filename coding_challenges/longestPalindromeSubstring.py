"""
Leetcode #5: Longest Palindromic Substring

Solved using Dynamic Programming.
Proof of Optimal Substructure and Overlapping Subproblems:
let i & j be index of the start and end of an input string S:

isPalindrome(S,i,j)={
                        False if S[i]!=S[j]
                        True if S[i]==S[j] AND isPalindrome(S,i+1,j-1)
                    }
"""
def longestPalindrome(s):
        sLen=len(s)
        if sLen==0:
            return ""
        table=[[0 for i in range(sLen)] for x in range(sLen)]
        maxP=s[0]
        table[sLen-1][sLen-1]=1
        for i in range(sLen-1):
            table[i][i]=1
            if s[i]==s[i+1]:
                table[i][i+1]=1
                maxP=s[i:i+2]
        for i in range(2,sLen):
            for j in range(i,sLen):
                if s[j]==s[j-i] and table[j-i+1][j-1]:
                    table[j-i][j]=1
                    if len(maxP)<len(s[j-i:j+1]):
                        maxP=s[j-i:j+1]
        return maxP
