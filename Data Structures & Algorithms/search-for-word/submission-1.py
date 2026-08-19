class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        self.directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        self.row_len = len(board)
        self.col_len = len(board[0])
        self.seen = set()
        for r in range(self.row_len):
            for c in range(self.col_len):
                if board[r][c] == word[0]:
                    self.seen.add((r,c))
                    if self.dfs(r,c, 1):
                        return True
                    self.seen.remove((r,c))
        return False
    def dfs(self, r1, c1, idx):
        if idx == len(self.word):
            return True
        for r2, c2 in self.directions:
            row = r1+r2
            col = c1+c2
            if row >= self.row_len or row < 0 or col <0 or col >= self.col_len or (row, col) in self.seen:
                continue
            if self.board[row][col] == self.word[idx]:
                self.seen.add((row, col))
                if self.dfs(row,col, idx+1):
                    return True
                self.seen.remove((row, col))