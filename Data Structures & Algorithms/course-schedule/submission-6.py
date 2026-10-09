class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_matrix = defaultdict(set)
        for course, dep in prerequisites:
            adj_matrix[course].add(dep)
        seen = set()
        dep_satisfied = set()
        
        def dfs(course):
            if course in dep_satisfied:
                return True
            if course in seen:
                return False
            seen.add(course)
            for each_dep in adj_matrix[course]:
                if not dfs(each_dep):
                    return False
            seen.remove(course)
            dep_satisfied.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True