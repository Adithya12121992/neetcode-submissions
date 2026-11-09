class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        seen = set()
        def dfs(r, c):
            for r1, c1 in directions:
                row = r+r1
                col = c+c1
                if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col] != '1' or (row, col) in seen:
                    continue
                seen.add((row, col))
                dfs(row, col)
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in seen:
                    seen.add((i, j))
                    dfs(i, j)
                    islands+=1
        return islands