# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []
        self.dfs(root)
        
        heapq.heapify(self.result)
        
        for i in range(k-1):
            heapq.heappop(self.result)
        return heapq.heappop(self.result)

    def dfs(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
