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
        cloned_graph = defaultdict(list)
        queue = deque([node])
        while queue:
            node_to_process = queue.popleft()
            if node_to_process not in cloned_graph:
                cloned_graph[node_to_process] = Node(node_to_process.val)
            for child in node_to_process.neighbors:
                if child not in cloned_graph:
                    queue.append(child)
                    cloned_graph[child] = Node(child.val)
                cloned_graph[node_to_process].neighbors.append(cloned_graph[child])
        return cloned_graph[node]
