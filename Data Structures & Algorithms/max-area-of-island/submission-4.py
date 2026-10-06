class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        result = -math.inf
        def dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for r1, c1 in directions:
                area += dfs(r1+r, c1+c)
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    # call dfs recursively and find all the connected elements
                    result = max(dfs(i, j), result)
        return result if result != -math.inf else 0

