class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        matrix = defaultdict(set)
        seen = set()
        completed_course = set()

        for course, dep in prerequisites:
            matrix[course].add(dep)
        
        def dfs(course):
            if course in completed_course:
                return True
            if course in seen:
                return False
            seen.add(course)
            for each_dep in matrix[course]:
                if not dfs(each_dep):
                    return False
            seen.remove(course)
            completed_course.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True