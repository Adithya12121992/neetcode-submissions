# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dict1 = -math.inf
        self.dfs(root)
        return self.dict1
    def dfs(self, root):
        if not root:
            return 0
        left_sub = max(self.dfs(root.left),0)
        right_sub = max(self.dfs(root.right),0)

        self.dict1 = max(left_sub+root.val+right_sub, self.dict1 )
        return root.val + max(left_sub, right_sub)