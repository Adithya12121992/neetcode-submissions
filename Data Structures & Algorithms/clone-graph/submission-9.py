"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned_graph = {}
        queue = deque([node])
        if not node:
            return 
        while queue:
            popped_elem = queue.popleft()
            if popped_elem not in cloned_graph:
                cloned_graph[popped_elem] = Node(popped_elem.val)
            for nei in popped_elem.neighbors:
                if nei not in cloned_graph:
                    cloned_graph[nei] = Node(nei.val)
                    queue.append(nei)
                cloned_graph[popped_elem].neighbors.append(cloned_graph[nei])
        return cloned_graph[node]