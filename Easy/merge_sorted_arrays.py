""" Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 are m and n respectively. 
    You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2. """

def mergeList2(nums1, m, nums2, n):
    # In this solution I started from scratch and simply created a new array and then copied it onto the first array.
    num = []
    for i in range(m):
        num.append(nums1[i])
    for i in range(n):
        num.append(nums2[i])
    num = sorted(num)
    nums1[:] = num[:]
    return nums1

def mergeList1(nums1, m, nums2, n):
    while m > 0 and n > 0:
        # Want to check if the last number of the first array is greater or equal to the last of the second array. If it is then 
        # move that greater integer to the end of the first array. Remove 1 from m to proceed to the next number.
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
        # Otherwise, we check if the number in the second array is greater. If it is then we set that number to the next spot at the end
        # of the first array. Proceed to remove 1 from n to continue to the next element.
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    # This line checks if there are anymore unchecked numbers in the second array. If so then that means the remaining elements 
    # were smaller than the other elements int he first array. Therefore, they need to be in the beginning of the first array.
    if n > 0:
        nums1[:n] = nums2[:n]

def mergeList(nums1, m, nums2, n):
    # Similar solution to the first but I copy with slicing instead of iterating with a for loop. 
    # It is a faster solution but uses more storage than the first solution.
    num = []
    num[:] = nums1[:m]
    num[m:] = nums2[:n]
    num.sort()
    nums1[:] = num[:]
    return nums1




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


