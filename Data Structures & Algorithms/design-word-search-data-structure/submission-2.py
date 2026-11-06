class ListNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_leaf = False
class WordDictionary:

    def __init__(self):
        self.root = ListNode(None)      

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = ListNode(char)
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_leaf
            if word[i] == '.':
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
                return False
            if word[i] not in node.children:
                return False
            else:
                return dfs(i+1, node.children[word[i]])
        curr = self.root
        return dfs(0, curr)
            
        
