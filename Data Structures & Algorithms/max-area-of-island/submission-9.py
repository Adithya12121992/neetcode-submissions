class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        result = 0
        def dfs(r, c):
            if (r,c) in seen:
                return
            seen.add((r,c))
            grid[r][c] = 0
            for r1, c1 in directions:
                row = r1+r
                col = c1+c
                if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col] == 0 or (row, col) in seen:
                    continue
                dfs(row, col)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    # call dfs recursively and find all the connected elements
                    seen = set()
                    dfs(i, j)
                    result = max(len(seen), result)
        return result

