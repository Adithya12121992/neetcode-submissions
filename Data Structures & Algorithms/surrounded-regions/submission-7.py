class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def flood(r, c):
            stack = [(r, c)]
            board[r][c] = 'T'
            while stack:
                r1, c1 = stack.pop()
                for dr, dc in directions:
                    row, col = r1 + dr, c1 + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 'O':
                        board[row][col] = 'T'
                        stack.append((row, col))

        for i in range(ROWS):
            for j in range(COLS):
                if (i in (0, ROWS-1) or j in (0, COLS-1)) and board[i][j] == 'O':
                    flood(i, j)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
