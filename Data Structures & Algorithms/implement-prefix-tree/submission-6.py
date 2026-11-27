class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_child = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                node = TreeNode(char)
                curr.children[char] = node
            curr = curr.children[char]
        curr.is_child = True

    def search(self, word: str, is_prefix=False) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        if is_prefix:
            return True
        return curr.is_child

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)
        