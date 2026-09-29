class TreeNode:
    def __init__(self, val= None):
        self.val = val
        self.is_leaf = False
        self.children = {}
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                childNode = TreeNode(char)
                curr.children[char] = childNode
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        return self.startsWith(word, True)
        

    def startsWith(self, prefix: str, check_leaf = False) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        if not check_leaf:
            return True
        else:
            return curr.is_leaf
