class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word = False
        self.word_name = None

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def insert_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TreeNode(ch)
            curr = curr.children[ch]
        curr.is_word = True
        curr.word_name = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_trie = Trie()
        res = set()
        for word in words:
            word_trie.insert_word(word)
        seen = set()

        def dfs(i, j, sub_word):
            seen.add((i, j))
            if sub_word.is_word:
                res.add(sub_word.word_name) 
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for r, c in directions:
                row = r+i
                col = c+j
                if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or (row, col) in seen or board[row][col] not in sub_word.children:
                    continue
                dfs(row, col, sub_word.children[board[row][col]])
            seen.remove((i, j))
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in word_trie.root.children:
                    dfs(i, j, word_trie.root.children[board[i][j]])
        return list(res) if res else []
        
        