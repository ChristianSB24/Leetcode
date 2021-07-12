# def arrayPairSum(nums):
#         maxMin = 0
#         nums.sort()
#         # print(nums)
#         # print(int((len(nums)/2)))
#         for i in range(int((len(nums)/2))):
#             # print(nums[2*i])
#             maxMin += nums[2*i]
#             print(maxMin)
#         return maxMin

def arrayPairSum(nums):
    nums.sort()
    return sum(nums[0::2])


# nums = [1,4, 3, 2]
nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))