"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dict1 = {}   
        dict1[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in dict1:
                    dict1[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                dict1[curr].neighbors.append(dict1[neighbor])
        return dict1[node]