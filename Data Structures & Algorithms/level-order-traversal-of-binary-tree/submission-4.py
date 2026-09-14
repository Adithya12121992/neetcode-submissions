# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dict1 = defaultdict(list)
        self.max_val = -math.inf
        self.dfs(root, 0)
        return_list = []
        if self.max_val == -math.inf:
            return []
        for i in range(self.max_val+1):
            return_list.append(self.dict1[i])
        return return_list
    def dfs(self, root, level):
        if not root:
            return
        self.dfs(root.left, level+1)
        self.dict1[level].append(root.val)
        self.max_val = max(self.max_val, level)
        self.dfs(root.right, level+1)        