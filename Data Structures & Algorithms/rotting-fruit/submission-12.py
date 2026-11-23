class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh_fruit_cnt = 0
        queue = deque()
        time_taken = -math.inf
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_fruit_cnt+=1
        if fresh_fruit_cnt ==0:
            return 0
        while queue:
            r1, c1, t1 = queue.popleft()
            for r2, c2 in directions:
                row = r1+r2
                col = c1+c2
                if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col]!=1:
                    continue
                grid[row][col] = 2
                fresh_fruit_cnt-=1
                queue.append((row, col, t1+1))
            time_taken = max(t1, time_taken)

        return time_taken if not fresh_fruit_cnt else -1