""" Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 are m and n respectively. 
    You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2. """

# def mergeList(nums1, m, nums2, n):
#     p = 0
#     if n == 0:
#         return sorted(nums1)
#     for i in range(len(nums1)):
#         if nums1[i - p] == 0:
#             nums1.pop(i - p)
#             p += 1
#     for x in nums2:
#         nums1.append(x)
#     return sorted(nums1)

def mergeList(nums1, m, nums2, n):
    counter = 0
    for i in nums1:
        for x in nums2:
            if x >= i:
                nums1.insert(nums1.index(i ), x)
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# nums1 = [1, 2, 3]
# nums2 = []
m = 3
# m = 3
n = 3
# n = 0
print(mergeList(nums1, m, nums2, n))


