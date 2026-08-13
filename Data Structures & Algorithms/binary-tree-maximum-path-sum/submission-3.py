# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dict1 = defaultdict(int)
        self.dfs(root)
        return max(self.dict1.values())
    def dfs(self, root):
        if not root:
            return 0
        left_branch = max(0, self.dfs(root.left))
        right_branch = max(0, self.dfs(root.right))
        self.dict1[root] = left_branch + right_branch + root.val
        return max(left_branch, right_branch) + root.val