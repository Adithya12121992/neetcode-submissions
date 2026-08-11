# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, [])[k-1]
    def dfs(self, root, list1):
        if not root:
            return 
        self.dfs(root.left, list1)
        list1.append(root.val)
        self.dfs(root.right, list1)
        return list1