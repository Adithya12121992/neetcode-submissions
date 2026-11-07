class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = None
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TreeNode(None)
    
    def _insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode(char)
            curr = curr.children[char]
        curr.is_leaf = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        word_trie = Trie()
        for word in words:
            if len(word)> ROWS*COLS:
                continue
            word_trie._insert(word)
        

        seen = set()
        result = set()
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]

        def dfs(r, c , trie_word):
            if trie_word.is_leaf:
                result.add(trie_word.word)
            for r1, c1 in directions:
                row = r+r1
                col = c+c1
                if row<0 or col<0 or row>=ROWS or col>=COLS or (row, col) in seen or board[row][col] not in trie_word.children:
                    continue
                seen.add((row, col))
                dfs(row, col, trie_word.children[board[row][col]])
                seen.remove((row, col))
            return False


        for i in range(ROWS):
            for j in range(COLS):
                word_to_search = board[i][j]
                if word_to_search in word_trie.root.children:
                    seen.add((i, j))
                    dfs(i, j , word_trie.root.children[word_to_search])
                    seen.remove((i, j))
                else:
                    continue
        return list(result) if result else []