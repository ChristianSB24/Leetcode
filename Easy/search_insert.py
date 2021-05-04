""" Faster than 89.26% of all Python submissions. Uses less memory than 79.63% of all Python submissions.
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order. """

def searchIn(nums, target):
    if target < min(nums):
        return 0
    if target > max(nums):
        return nums.index(max(nums)) + 1
    for i in range(len(nums)):
        if i == 0 and nums[0] == target:
            return 0
        if nums[i] == target:
            return i
        if target > nums[i - 1] and target < nums[i]:
            return i

        