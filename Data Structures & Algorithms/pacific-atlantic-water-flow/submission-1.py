class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # solve for pacific ocean cells first 
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            if ((r,c) in visit or 
            r< 0 or c<0 or r>=rows or c >= cols
            or heights[r][c]<prevHeight):
                return 
            visit.add((r, c))
            for r1, c1 in directions:
                dfs(r1+r, c1+c, visit, heights[r][c])
        
        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])
        res = atlantic & pacific
        return list(res)


