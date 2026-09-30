class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()
        def dfs(r, c):
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            seen.add((r,c))
            for r1, c1 in directions:
                row = r+r1
                col = c+c1
                if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or (row, col) in seen or grid[row][col]!='1':
                    continue
                dfs(row, col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in seen:
                    dfs(i, j)
                    islands+=1
        return islands