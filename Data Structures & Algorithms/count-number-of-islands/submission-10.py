class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        def dfs(r, c):
            grid[r][c] = '0'
            for r1, c1 in directions:
                row = r+r1
                col = c+c1

                if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col] != '1':
                    continue
                dfs(row, col)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands+=1
        return islands