# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        ptr1 = head
        ptr2 = head.next

        while ptr2 and ptr2.next:
            if ptr1 == ptr2:
                return True
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return False