# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(-math.inf, root, math.inf)
    def dfs(self, start, root, end):
        if not root:
            return True
        if start < root.val < end:
            return True and self.dfs(start, root.left, root.val) and self.dfs(root.val, root.right, end)
        else:
            return False
        