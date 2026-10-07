class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        ripe_bananas = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    ripe_bananas.append((i,j))
        result = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            r, c, t0 = queue.popleft()
            for r1, c1 in directions:
                row, col = r1+r, c1+c
                if row<0 or row>=ROWS or col<0 or col>=COLS or grid[row][col]!=1:
                    continue
                grid[row][col] = 2
                queue.append((row, col, t0+1))
            result = max(result, t0)
        for i, j in ripe_bananas:
            if grid[i][j] !=2:
                return -1
        return result