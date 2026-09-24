class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def dfs(r, c , index):
            if index >=len(word):
                return True
            seen.add((r,c))
            directions = [(0,1), (1,0), (0,-1), (-1, 0)]
            for r1, c1 in directions:
                row = r1+r
                col = c1+c

                if row<0 or col<0 or row>=len(board) or col>=len(board[0]) or (row, col) in seen or board[row][col]!=word[index]:
                    continue
                if dfs(row, col, index+1):
                    return True
            seen.remove((r, c))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== word[0]:
                    if dfs(i, j, 1):
                        return True
        return False
