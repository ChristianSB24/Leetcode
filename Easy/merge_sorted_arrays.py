""" Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 are m and n respectively. 
    You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2. """

def mergeList(nums1, m, nums2, n):
    num = []
    for i in range(m + n):
        num.append(nums1[i])
    for i in range(n):
        num.append(nums2[i])
    num = sorted(num)
    for i in range(m + n):
        nums1[i] = num[i]
    return nums1

# def mergeList(nums1, m, nums2, n):
#     for i in range(n):
#         if nums2[i] <= max(nums1):
#             for x in range(m):
#                 if nums1[x] <= nums2[i] <= nums1[x + 1]:
#                     nums1.insert(nums1.index(nums1[x] + 1), nums2[i])
#                     break
#         else:
#             nums1.insert(nums1.index(0), nums2[i])
#     for i in nums1:
#         if i == 0:
#             nums1.pop(nums1.index(i))
#     nums1.remove(0)
#     return nums1




nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# nums1 = [1, 2, 3]
# nums2 = []
# nums1 = [0]
# nums2 = [1]
# m = 0
# n = 1
# m = 3
m = 3
n = 3
# n = 0
print(mergeList(nums1, m, nums2, n))


