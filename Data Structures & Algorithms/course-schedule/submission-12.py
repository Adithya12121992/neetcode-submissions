class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for src, dep in prerequisites:
            adj_list[src].append(dep)
        
        # 3 things to note
        # 1 : cycle detection is needed --> return False
        # 2 : All conditions for a particular course are not met --> returen False
        # 3 : All conditions for a particular course are met --> continue with next course and to the end return True

        # since the courses are numbered from 0 to numCourses-1
        visiting = set()
        def dfs(course):
            if course in visiting:
                # cycle detected
                return False
            if course not in adj_list:
                return True
            visiting.add(course)
            for pre_req in adj_list[course]:
                if not dfs(pre_req):
                    return False
            visiting.remove(course)
            adj_list[course] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True