""" Given an integer array nums of 2n integers, group these integers into n pairs 
    (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum. """

# This is the bruteforce method that cycles through each pair of elements and adds it to maxMin. It is a slow solution because
# it uses the functions range(), int(), and len(). If there is a way to remove these it would be much faster.
# def arrayPairSum(nums):
#         maxMin = 0
#         nums.sort()
#         for i in range(int((len(nums)/2))):
#             maxMin += nums[2*i]
#         return maxMin

# This is a simple solution that could be simplified more by using sorted instead of sort that would make it a one liner.
# Not much faster though, I need to do more research but I believe that the function sum() and the process of slicing the list
# takes a lot of time. If these could be removed we could optimize it further.
# def arrayPairSum(nums):
#     nums.sort()
#     return sum(nums[0::2])

# This is the fastest solution of the three since it does not make any copies of the list or use any other functions.
# There is only 2 variables, s and i. Through each cycle we add to those variables only as much as we need to.
# This saves time and space since there are no copies or additional functions. 
def arrayPairSum(nums):
    nums.sort()
    s=0
    i=0
    while i<=len(nums)-1:
        s+=nums[i]
        i+=2
    return s


# nums = [1,4, 3, 2]
nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))