""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)). """

def medList(nums1, nums2):
    nums1[len(nums1):] = nums2[:]
    nums1.sort()
    print(nums1)
    if len(nums1) % 2 != 0:
        return nums1[int((len(nums1) + 1) / 2) - 1]
    else:
        return (nums1[int((len(nums1) / 2)) - 1] + nums1[int(((len(nums1) / 2) + 1)) - 1]) / 2
