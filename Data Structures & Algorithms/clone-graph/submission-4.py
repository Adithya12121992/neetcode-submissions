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
        graph = defaultdict(list)
        q = deque([node])
        while q:
            popped_item = q.popleft()
            if popped_item not in graph:
                graph[popped_item] = Node(popped_item.val)
            for nei in popped_item.neighbors:
                if nei not in graph:
                    graph[nei] = Node(nei.val)
                    q.append(nei)
                graph[popped_item].neighbors.append(graph[nei])
        return graph[node]

