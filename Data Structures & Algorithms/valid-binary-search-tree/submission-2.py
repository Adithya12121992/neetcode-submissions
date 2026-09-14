# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ret_val = True
        self.dfs(-math.inf, root, math.inf)
        return self.ret_val
    def dfs(self, min_val, root, max_val):
        if not root:
            return 
        
        self.dfs(min_val, root.left, root.val)
        if not(min_val < root.val < max_val):
            self.ret_val = self.ret_val and False
        self.dfs(root.val, root.right, max_val)