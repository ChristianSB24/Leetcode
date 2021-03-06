""" Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists. """

# def mergeList(l1, l2):
#     l3 = []
#     for i in l1:
#         l3.append(i)
#     for i in l2:
#         l3.append(i)
#     return sorted(l3)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists1(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
