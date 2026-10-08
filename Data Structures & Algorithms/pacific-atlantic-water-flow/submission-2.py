class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_set = set()
        atlantic_set = set()    
        directions = [(0, 1), (1, 0), (-1, 0), (0,-1)]
        def dfs(r, c, visit, prevHeight):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            if ((r,c) in visit or r< 0 or c<0 or r>=ROWS or c >= COLS or heights[r][c]<prevHeight):
                return 
            visit.add((r, c))
            for r1, c1 in directions:
                dfs(r1+r, c1+c, visit, heights[r][c])
        for j in range(len(heights[0])):
            dfs(0, j, pacific_set, heights[0][j])
            dfs(ROWS-1, j, atlantic_set, heights[ROWS-1][j])
        for i in range(len(heights)):
            dfs(i, 0, pacific_set, heights[i][0])
            dfs(i, COLS-1, atlantic_set, heights[i][COLS-1])
        return list(pacific_set & atlantic_set)
