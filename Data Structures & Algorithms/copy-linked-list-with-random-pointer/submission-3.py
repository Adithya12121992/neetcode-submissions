"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        dict1 = {}
        node_to_idx = {}
        curr = head
        idx = 0
        while curr:
            dict1[idx] = Node(curr.val)
            node_to_idx[curr] = idx
            curr = curr.next
            idx+=1
        curr = head
        idx = 0
        while curr:
            dict1[idx].next = dict1[idx+1] if idx+1 in dict1.keys() else None
            if curr.random is not None:
                random_node_idx = node_to_idx[curr.random]
                dict1[idx].random = dict1[random_node_idx]
            else:
                dict1[idx].random = None
            curr = curr.next
            idx+=1
        return dict1[0]