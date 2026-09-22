class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            grid[r][c] = '0'
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for r1, c1 in directions:
                row = r+r1
                col = c+c1
                if row <0 or row>=len(grid) or col <0 or col>=len(grid[0]) or grid[row][col]!='1':
                    continue
                dfs(row, col)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=="1":
                    dfs(r,c)
                    res+=1
        return res