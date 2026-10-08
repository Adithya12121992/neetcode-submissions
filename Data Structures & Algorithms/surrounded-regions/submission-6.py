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
                cr, cc = stack.pop()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                        board[nr][nc] = 'T'   # mark on push
                        stack.append((nr, nc))

        # 1. start from borders only
        for i in range(ROWS):
            for j in range(COLS):
                if (i in (0, ROWS-1) or j in (0, COLS-1)) and board[i][j] == 'O':
                    flood(i, j)

        # 2 & 3. flip
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
