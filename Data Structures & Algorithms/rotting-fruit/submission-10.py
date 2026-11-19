class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh_cnt = 0
        time_taken = -1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_cnt+=1
        if fresh_cnt == 0:
            return 0
        while queue:
            r2, c2, interim_time = queue.popleft()
            for r1, c1 in directions:
                row = r1+r2
                col = c1+c2

                if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col]!=1:
                    continue
                grid[row][col] = 2
                queue.append((row, col, interim_time+1))
            time_taken = max(time_taken, interim_time)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return time_taken
        # now , i have all the rotten bananas list with me
        # the plan is run dfs for each of the rotten banans while incrementing the count by 1. at the end if there is no rotten banana then record the count as max_cnt.
