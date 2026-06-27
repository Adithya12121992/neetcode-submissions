class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we solve for rows 
        row_dict1 = defaultdict(set)
        col_dict1 = defaultdict(set)
        block_dict1 = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]

                if val=='.':
                    continue
                if val in row_dict1[i]:
                    return False
                else:
                    row_dict1[i].add(val)

                if val in col_dict1[j]:
                    return False
                else:
                    col_dict1[j].add(val)


                if val in block_dict1[(i//3, j//3)]:
                    return False
                else:
                    block_dict1[(i//3, j//3)].add(val)
        return True