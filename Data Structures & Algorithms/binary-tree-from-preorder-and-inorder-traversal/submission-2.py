# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # get the root from preorder , divide the tree into left sub and right sub from inorder 
        inorder_dict = {val:idx for idx, val in enumerate(inorder)}

        def dfs(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            in_root_idx = inorder_dict[root_val]
            left_size = in_root_idx - in_start
            root.left = dfs(pre_start+1, pre_start+left_size, in_start, in_root_idx-1)
            root.right = dfs(pre_start+1+left_size, pre_end , in_root_idx+1, in_end)
            return root
        
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)