# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ret_val = 0
        self.dfs(root, 1)
        return self.ret_val
    def dfs(self, root, level):
        if not root:
            return
        
        self.dfs(root.left, level+1)
        self.ret_val = max(self.ret_val, level)
        self.dfs(root.right, level+1)
    
