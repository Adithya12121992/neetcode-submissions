"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return 
        cloned_graph = {}
        queue = deque([root])
        while queue:
            curr_node = queue.popleft()
            if curr_node not in cloned_graph:
                cloned_graph[curr_node] = Node(curr_node.val)
            for nei in curr_node.children:
                if nei not in cloned_graph:
                    cloned_graph[nei] = Node(nei.val)
                    queue.append(nei)
                cloned_graph[curr_node].children.append(cloned_graph[nei])
        return cloned_graph[root]
