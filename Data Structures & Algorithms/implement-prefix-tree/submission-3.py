class TreeNode:
    def __init__(self, val):
        self.node = val
        self.is_leaf = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for elem in word:
            if elem in curr.children:
                curr = curr.children[elem]
            else:
                childNode = TreeNode(elem)
                curr.children[elem] = childNode
                curr = curr.children[elem]
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        return self.startsWith(word, True)

    def startsWith(self, prefix: str, check_leaf=False) -> bool:
        curr = self.root
        for elem in prefix:
            if elem not in curr.children:
                return False
            else:
                curr = curr.children[elem]
        if not check_leaf:
            return True
        else:
            return curr.is_leaf
        