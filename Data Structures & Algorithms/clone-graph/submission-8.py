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
        if not node:
            return None
        queue = deque([node])
        while queue:
            node_to_process = queue.popleft()
            if node_to_process not in cloned_graph:
                cloned_graph[node_to_process] = Node(node_to_process.val)
            for nei in node_to_process.neighbors:
                if nei not in cloned_graph:
                    cloned_graph[nei] = Node(nei.val)
                    queue.append(nei)
                cloned_graph[node_to_process].neighbors.append(cloned_graph[nei])
        return cloned_graph[node]