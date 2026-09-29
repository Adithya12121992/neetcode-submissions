class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.children= {}
        self.is_leaf = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TreeNode(ch)
            curr = curr.children[ch]
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i==len(word):
                return curr.is_leaf
            ch = word[i]
            if ch == '.':
                for child in curr.children:
                    if dfs(i+1, curr.children[child]):
                        return True
                return False
            if ch in curr.children:
                return dfs(i+1, curr.children[ch])
            else:
                return False
        curr =self.root
        return dfs(0, curr)
            
            
        
    
        
