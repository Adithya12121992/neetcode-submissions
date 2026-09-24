# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, each_queue in enumerate(lists):
            if each_queue:
                heapq.heappush(heap, [each_queue.val, idx, each_queue])
        mainNode = ListNode()
        curr = mainNode
        while heap:
            val, idx, node = heapq.heappop(heap)
            if lists[idx] and lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, [lists[idx].val, idx, lists[idx]])
            curr.next = node
            curr = node
        return mainNode.next