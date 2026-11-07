class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        if len(word)> ROWS * COLS:
            return False
        def dfs(r, c, idx):
            if idx>=len(word):
                return True
            for r1, c1 in directions:
                row = r+r1
                col = c+c1
                if row<0 or col<0 or row>=ROWS or col>=COLS or (row, col) in seen or board[row][col]!=word[idx]:
                    continue
                seen.add((row, col))
                if dfs(row, col, idx+1):
                    return True
                seen.remove((row, col))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False