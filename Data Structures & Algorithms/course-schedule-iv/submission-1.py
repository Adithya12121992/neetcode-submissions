class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #def check_for_deps(course1, course2):
        graph = defaultdict(set)
        for course, dep_course in prerequisites:
            graph[dep_course].add(course)
        memo = {}
        def check_for_deps(course1, course2):
            if (course1, course2) in memo:
                return memo[(course1, course2)]
            result = False
            dep_courses = graph[course2]
            for each_dep in dep_courses:
                if each_dep == course1 or check_for_deps(course1, each_dep):
                    result = True
                    break
            memo[(course1, course2)] = result
            return result
        res = []
        for c1, c2 in queries:
            res.append(check_for_deps(c1, c2))
        return res
                