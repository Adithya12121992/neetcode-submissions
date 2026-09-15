class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        seen = set()
        def dfs(r, c):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for r1, c1 in directions:
                row = r1+r
                col = c1+c
                if row >= len(grid) or row< 0 or col>=len(grid[0]) or col <0 or (row, col) in seen or grid[row][col]!="1":
                    continue
                seen.add((row, col))
                dfs(row, col)
                
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    if (r,c) in seen:
                        continue
                    seen.add((r,c))
                    dfs(r,c)
                    result +=1
        
        return (result)
