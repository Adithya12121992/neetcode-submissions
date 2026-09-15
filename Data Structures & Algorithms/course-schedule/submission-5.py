class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps_satisfied = set()
        visiting = set()
        deps = defaultdict(set)
        def dfs(course):
            if course in visiting:
                return False
            if course in deps_satisfied:
                return True
            visiting.add(course)
            for each_dep in deps[course]:
                if not dfs(each_dep):
                    return False
            visiting.remove(course)
            deps_satisfied.add(course)
            return True

        for a,b in prerequisites:
            deps[a].add(b)
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
