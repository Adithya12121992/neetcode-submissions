class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_leaf = False
class PrefixTree:

    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode(char)
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.is_leaf
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True
        
        