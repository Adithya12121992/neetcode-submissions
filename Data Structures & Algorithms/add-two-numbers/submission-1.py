# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reverse_l1 = l1
        reverse_l2 = l2
        carry = 0
        mainNode = ListNode()
        curr = mainNode
        while reverse_l1 or reverse_l2 or carry:
            sum1 = 0
            if reverse_l1 and reverse_l2:
                sum1 = reverse_l1.val + reverse_l2.val
                reverse_l1 = reverse_l1.next
                reverse_l2 = reverse_l2.next
            elif reverse_l1:
                sum1 = reverse_l1.val
                reverse_l1 = reverse_l1.next
            elif reverse_l2:
                sum1 = reverse_l2.val
                reverse_l2 = reverse_l2.next
            carry, sum1 = divmod(sum1+carry, 10)
            curr.next = ListNode(sum1)
            curr = curr.next
        return mainNode.next
