class Tree:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.endofWord = False

class PrefixTree:

    def __init__(self):
        self.root = Tree()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Tree(ch)
            curr = curr.children[ch]
        curr.endofWord = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return curr.endofWord


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return True

