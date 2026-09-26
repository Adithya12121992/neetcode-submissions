# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        truth_matrix = [False for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if knows(i, j):
                    truth_matrix[i] = True # the person knows someone, check rule 1 
                    break
        # check if every one knows him
        for i in range(n):
            if not truth_matrix[i]:
                is_celebrity= True
                for j in range(n):
                    if i==j:
                        continue
                    is_celebrity = is_celebrity and knows(j, i)
                if is_celebrity:
                    return i
        return -1