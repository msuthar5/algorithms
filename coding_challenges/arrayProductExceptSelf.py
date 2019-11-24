"""
Leetcode #238: Array Product Except Self

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].
"""
def productHelper(nums,i,left):
    if i == len(nums):
        return 1
    right=productHelper(nums,i+1,left*nums[i])
    tmp=nums[i]
    nums[i]=left*right
    return right*tmp

def productExceptSelf(nums):
    productHelper(nums,0,1)
    return nums
