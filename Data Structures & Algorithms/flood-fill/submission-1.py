class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1), (1,0), (-1, 0), (0,-1)]
        ROWS = len(image)
        COLS = len(image[0])
        start_color = image[sr][sc]
        seen = set()
        '''queue = deque([(sr, sc)])
        while queue:
            r,c = queue.popleft()
            seen.add((r,c))
            image[r][c] = color
            for r1, c1 in directions:
                row = r1+r
                col = c1+c
                if row <0 or row>=ROWS or col <0 or col>=COLS or image[row][col]!=start_color or (row, col) in seen:
                    continue
                queue.append([row, col])
        return image'''
        def dfs(r, c):
            if (r, c) in seen:
                return 
            image[r][c] = color
            seen.add((r,c))
            for r1, c1 in directions:
                row = r1+r
                col = c1+c
                if row <0 or row>=ROWS or col <0 or col>=COLS or image[row][col]!=start_color or (row, col) in seen:
                    continue
                dfs(row, col)
        dfs(sr,sc)
        return image