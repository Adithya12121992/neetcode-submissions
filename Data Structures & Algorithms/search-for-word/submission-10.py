class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        to_traverse = []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])
        if len(word)>ROWS*COLS:
            return False
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    to_traverse.append((i, j))
        def dfs(r1, c1 , k):
            if k >= len(word):
                return True
            for r2, c2 in directions:
                row = r1+r2
                col = c1+c2
                if row<0 or row>=ROWS or col<0 or col>=COLS or board[row][col]!=word[k] or (row, col) in seen:
                    continue
                else:
                    seen.add((row, col))
                    if dfs(row, col, k+1):
                        return True
                    seen.remove((row, col))
            return False
        
        for r, c in to_traverse:
            if dfs(r, c, 1):
                return True
        return False