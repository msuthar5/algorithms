"""
Leetcode #3: Length of Longest Substring Without Repeating Characters

56 ms faster than 92% of submissions
12.8 MB less than 100% of submissions
"""
def lengthOfLongestSubstring(s: str) -> int:
    if len(s)<2:
        return len(s)
    maxLen=0
    l=len(s)
    d=dict()
    i=j=0
    while j < l:
        if s[j] in d:
            maxLen=max(maxLen,j-i)
            i=max(d[s[j]]+1,i)
        d[s[j]]=j
        j+=1
    return max(maxLen,j-i)
