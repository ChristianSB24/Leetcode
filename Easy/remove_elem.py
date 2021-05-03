""" Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well. """

""" Slow solution """
# def remElem(nums, val):
#     l = len(nums)
#     counter = 0
#     for i in range(len(nums)):
#         if nums[i - counter] == val:
#             nums.pop(i - counter)
#             counter += 1
#     return l - counter 

""" The leetcode website seems to not recognize the .reverse() method from python so this solution doesnt work. 
    My tests seem to work though. """
# def remElem(nums, val):
#     counter = 0
#     count = 0
#     nums = sorted(nums)
#     for i in nums:
#         if i == val:
#             counter += 1
#     for i in range(len(nums)):
#         if nums[i - count] != val:
#             nums.append(nums[i - count])
#             nums.remove(nums[i - count])
#             count += 1
#         else:
#             nums.reverse()
#             print(nums)
#             return len(nums) - counter

""" Faster than 90.94% of all Python solutions. Memory usage beats 77.55% of all solutions. """
def remElem(nums, val):
    counter = 0
    # Want to have all elements on left side of list except for the elements we don't want we put on the right side. 
    # We do this by using pop to remove them and then add them to the end of the list.
    # Need to adjust the index we refer to because when we remove an element the elements ahead of it have an index minus 1.
    # We do this with the counter variable. Finally, return the length of the list without the elements we do not want.
    for i in range(len(nums)):
        if nums[i - counter] == val:
            nums.append(nums.pop(i - counter))
            counter += 1
    return len(nums) - counter

