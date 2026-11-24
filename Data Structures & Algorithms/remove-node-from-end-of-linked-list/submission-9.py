# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length+=1
            curr = curr.next
        to_iter = length-n
        curr = head
        if to_iter<=0:
            return head.next
        for _ in range(to_iter-1):
            curr = curr.next
        curr.next = curr.next.next
        return head