"""
Leetcode #78: Subsets

Generate a powerset from the input list
powerset of n elements consists of 2^n subsets
"""
def subsets(nums):
    s=list()
    d=dict()
    def setGen(nums):
        if str(nums) in d:
            return
        s.append(nums)
        d[str(nums)]=True
        for i in range(len(nums)):
            setGen(nums[:i]+nums[i+1:])
    setGen(nums)
    return s
