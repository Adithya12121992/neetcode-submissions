# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        list1 = []
        if not root:
            return ""
        def dfs(root1):
            if not root1:
                list1.append('#')
                return
            list1.append(str(root1.val))
            dfs(root1.left)
            dfs(root1.right)
        dfs(root)
        return ",".join(list1)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()