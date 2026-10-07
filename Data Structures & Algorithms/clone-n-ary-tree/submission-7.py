"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        curr = root
        queue = deque([curr])
        cloned_graph = {}
        while queue:
            node = queue.popleft()
            if node and node not in cloned_graph:
                cloned_graph[node] = Node(node.val)
            if node and node.children:
                for child in node.children:
                    queue.append(child)
                    if child not in cloned_graph:
                        cloned_graph[child] = Node(child.val)
                    cloned_graph[node].children.append(cloned_graph[child])
        return cloned_graph[root] if root else None

