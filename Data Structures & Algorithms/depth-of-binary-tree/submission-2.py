# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth
    def dfs(self, root, level):
        if not root:
            return 
        self.dfs(root.left, level+1)
        self.max_depth = max(self.max_depth, level)
        self.dfs(root.right, level+1)