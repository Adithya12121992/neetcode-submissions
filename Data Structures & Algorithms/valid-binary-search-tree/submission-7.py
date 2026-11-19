# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(min_val, root, max_val):
            if not root:
                return True
            if min_val<root.val<max_val:
                left = dfs(min_val, root.left, root.val)
                right = dfs(root.val, root.right, max_val)
                return left and right
            else:
                return False
        return dfs(-math.inf, root, math.inf)