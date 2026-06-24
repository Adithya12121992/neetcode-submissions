# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        mainNode = ListNode()
        mainNode.next = head
        curr = head
        while curr:
            total+=1
            curr = curr.next
        element_to_remove = total-n
        cnt = 0
        if element_to_remove == 0:
            return head.next
        while cnt < element_to_remove-1:
            head = head.next
            cnt+=1
        head.next = head.next.next
        return mainNode.next
