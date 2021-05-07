""" Given an integer array nums, find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum."""

# def maxSub(nums):
#     sums = []
#     if len(nums) == 1:
#         return nums[0]
#     if all(x > -1 for x in nums):
#         return sum(nums)
#     if all(x < 0 for x in nums):
#         return sum(nums)
#     for i in range(len(nums)):
#         counter = 1
#         for x in range(len(nums)):
#             if nums[i: x + counter] == []:
#                 continue
#             sums.append(sum(nums[i:x + counter]))
#         counter += 1
#     return max(sums)

def maxSub(nums):
    



# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
# nums = [-2,-1]
nums = [1, 0, 3, 4, 6]
print(maxSub(nums))