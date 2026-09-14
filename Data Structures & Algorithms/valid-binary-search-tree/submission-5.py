# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(-math.inf, root, math.inf)
    def dfs(self, min_val, root, max_val):
        if not root:
            return True
        if not(min_val < root.val < max_val):
            return False
        return self.dfs(root.val, root.right, max_val) and self.dfs(min_val, root.left, root.val)