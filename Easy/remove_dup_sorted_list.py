""" Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well. """

def deleteDuplicate(head):
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next     # skip duplicated node
        cur = cur.next     # not duplicate of current node, move to next node
    return head