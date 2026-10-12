class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        islands = 0
        def dfs(r, c):
            if (r,c) in seen:
                return
            seen.add((r,c))
            for r1, c1 in directions:
                row = r+r1
                col = c+c1
                if row<0 or row>=ROWS or col<0 or col>=COLS or (row, col) in seen or grid[row][col]!='1':
                    continue
                dfs(row, col)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in seen:
                    dfs(i, j)
                    islands+=1
        return islands