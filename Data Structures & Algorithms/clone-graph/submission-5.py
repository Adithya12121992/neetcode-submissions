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
        queue =deque([node])
        while queue:
            curr_node = queue.popleft()
            if curr_node not in cloned_graph:
                cloned_graph[curr_node] = Node(curr_node.val)
            for nei in curr_node.neighbors:
                if nei not in cloned_graph:
                    cloned_graph[nei] = Node(nei.val)
                    queue.append(nei)
                cloned_graph[curr_node].neighbors.append(cloned_graph[nei])
        return cloned_graph[node]