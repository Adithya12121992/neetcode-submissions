class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the rotten fruit first
        # if no rotten fruit , return -1 
        # if yes , iterate through them , use BFS to find all the other fresh fruti and mark them rotten, ensure to pass in the time t to each bfs to keep track of the time , and everytome you are done, update the max_time = max(max_time, t)
        # now check if there are any fresh fruit , if yes return -1 , if no return max_time
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        max_time = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            r, c, t = queue.popleft()
            for r1, c1 in directions:
                row = r1+r
                col = c1+c
                if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col]!=1:
                    continue
                queue.append((row, col, t+1))
                grid[row][col] = 2
            max_time = max(max_time, t)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return max_time