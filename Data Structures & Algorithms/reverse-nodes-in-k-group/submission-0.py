# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        # curr is at the next of the 1st group 
        
        prev = None
        group_curr = head
        for _ in range(k):
            temp = group_curr.next
            group_curr.next = prev
            prev = group_curr
            group_curr = temp
        head.next = self.reverseKGroup(curr, k)

        return prev