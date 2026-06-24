# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
        mainNode = ListNode()
        curr = mainNode
        while heap:
            val, idx, popped_node = heapq.heappop(heap)
            print(idx, popped_node.val)
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx, lists[idx]))
            curr.next = popped_node
            curr = curr.next
        return mainNode.next