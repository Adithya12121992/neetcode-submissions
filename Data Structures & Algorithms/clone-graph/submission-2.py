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
            return 
        cloned_graph = {}
        cloned_graph[node] = Node(node.val)
        q = deque([node])
        seen = set()
        while q:
            popped_node = q.popleft()
            for nei in popped_node.neighbors:
                if nei not in cloned_graph:
                    cloned_graph[nei] = Node(nei.val)
                    q.append(nei)
                cloned_graph[popped_node].neighbors.append(cloned_graph[nei])
        return cloned_graph[node]
        